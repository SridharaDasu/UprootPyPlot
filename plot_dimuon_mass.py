import sys
import uproot
import numpy as np
import vector
import matplotlib.pyplot as plt

if len(sys.argv) == 2:
    input_file = sys.argv[1]
else:
    input_file = "e+e-zh.root"

input = uproot.open(input_file)

events = input["Delphes;1"]

# Select events with at least two muons
dimuon_masses = []
for dimuon_event in events.arrays(["Muon/Muon.PT", "Muon/Muon.Eta", "Muon/Muon.Phi"], "Muon_size > 1"):
    # Construct four vectors of the two muons in the event
    muon0 = vector.obj(
        pt=dimuon_event['Muon/Muon.PT'][0],
        eta=dimuon_event['Muon/Muon.Eta'][0],
        phi=dimuon_event['Muon/Muon.Phi'][0],
        mass=0.105
    )
    muon1 = vector.obj(
        pt=dimuon_event['Muon/Muon.PT'][1],
        eta=dimuon_event['Muon/Muon.Eta'][1],
        phi=dimuon_event['Muon/Muon.Phi'][1],
        mass=0.105
    )
    # Create dimiuon
    dimuon =muon0 + muon1
    dimuon_masses.append(dimuon.mass)

fig, ax = plt.subplots()
fig.suptitle('Invariant mass of muon pairs')
ax.set_xlabel('Invariant mass of muon pairs (GeV)')
ax.set_ylabel('Events per GeV')
ax.hist(dimuon_masses, bins=200, linewidth=0.5, edgecolor="white")
ax.set(xlim=(0, 200))

plt.show()
