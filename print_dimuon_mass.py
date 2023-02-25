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
for dimuons in events.arrays(["Muon/Muon.PT", "Muon/Muon.Eta", "Muon/Muon.Phi"]):
    if len(dimuons["Muon/Muon.PT"]) > 1:
        # Construct four vectors of the two muons in the event
        muon0 = vector.obj(
            pt=dimuons['Muon/Muon.PT'][0],
            eta=dimuons['Muon/Muon.Eta'][0],
            phi=dimuons['Muon/Muon.Phi'][0],
            mass=0.105
        )
        muon1 = vector.obj(
            pt=dimuons['Muon/Muon.PT'][1],
            eta=dimuons['Muon/Muon.Eta'][1],
            phi=dimuons['Muon/Muon.Phi'][1],
            mass=0.105
        )
        # Print invariant mass
        dimuon = muon0 + muon1
        print(dimuon.mass)
