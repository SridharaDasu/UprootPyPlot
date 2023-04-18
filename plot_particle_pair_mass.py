from coffea import processor
from coffea.nanoevents.methods import candidate
import hist

class PairProcessor(processor.ProcessorABC):
    def __init__(self):
        pass

    def pair_mass(self, particle, particle_name="p", charged=False):
        if charged:
            particles = ak.zip(
                {
                    "pt": particle.PT,
                    "eta": particle.Eta,
                    "phi": particle.Phi,
                    "mass": particle.mass,
                    "charge": particle.Charge,
                },
                with_name="PtEtaPhiMCandidate",
                behavior=candidate.behavior,
            )
            # Check that there are two particle candidates and they are oppositely charged
            cut = (ak.num(particles) == 2) & (ak.sum(particles.charge, axis=1) == 0)
        else:
            particles = ak.zip(
                {
                    "pt": particle.PT,
                    "eta": particle.Eta,
                    "phi": particle.Phi,
                    "mass": particle.mass,
                    "charge": particle.mass,  # Dummy variable needed as photon does not have Charge variable
                },
                with_name="PtEtaPhiMCandidate",
                behavior=candidate.behavior,
            )
            # Check that there are two particle candidates, ignoring charge
            cut=ak.num(particles) == 2
        h_mass = (
            hist.Hist.new
            .Log(1000, 0.2, 200., name="mass", label=f"$m_{{{particle_name}{particle_name}}}$ [GeV]")
            .Int64()
        )
        pair = particles[cut][:, 0] + particles[cut][:, 1]
        h_mass.fill(mass=pair.mass)
        return h_mass

    def process(self, events):
        dataset = events.metadata["dataset"]
        h_m_pair_mass = self.pair_mass(events.Muon, "\mu", charged=True)
        h_e_pair_mass = self.pair_mass(events.Electron, "e", charged=True)
        h_j_pair_mass = self.pair_mass(events.Jet, "j", charged=False)
        h_p_pair_mass = self.pair_mass(events.Photon, "\gamma", charged=False)
        return {
            dataset: {
                "entries": len(events),
                "h_m_pair_mass": h_m_pair_mass,
                "h_e_pair_mass": h_e_pair_mass,
                "h_j_pair_mass": h_j_pair_mass,
                "h_p_pair_mass": h_p_pair_mass,
            }
        }

    def postprocess(self, accumulator):
        pass


import sys
import uproot
import awkward as ak
from coffea.nanoevents import NanoEventsFactory
from coffea.nanoevents import DelphesSchema
import matplotlib.pyplot as plt
if len(sys.argv) == 2:
    dataset = sys.argv[1]
else:
    dataset = "e+e-zh"
file = uproot.open(f"{dataset}.root")
events = NanoEventsFactory.from_root(
    file,
    schemaclass=DelphesSchema,
    treepath="Delphes",
    metadata={"dataset": dataset},
).events()
p = PairProcessor()
out = p.process(events)
fig, axs = plt.subplots(2, 2)
fig.suptitle(f"Particle Pair Masses ({dataset})")
out[dataset]['h_m_pair_mass'].plot1d(ax=axs[0, 0])
out[dataset]['h_e_pair_mass'].plot1d(ax=axs[0, 1])
out[dataset]['h_j_pair_mass'].plot1d(ax=axs[1, 0])
out[dataset]['h_p_pair_mass'].plot1d(ax=axs[1, 1])
plt.show()
fig.savefig(f"{dataset}.png")
