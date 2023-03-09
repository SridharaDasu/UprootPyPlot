import sys
import uproot
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) == 2:
    input_file = sys.argv[1]
else:
    input_file = "e+e-zh.root"

input = uproot.open(input_file)


# Hadronic transverse energy == Sum of Jet ETs
ht=np.squeeze(input["Delphes;1"]["ScalarHT"]["ScalarHT.HT"].array())
# Missing ET
met=np.squeeze(input["Delphes;1"]["MissingET"]["MissingET.MET"].array())
# Number of generated jets
ngjets=input["Delphes;1"]["GenJet_size"].array()
# Number of reconstructed jets
nrjets=input["Delphes;1"]["Jet_size"].array()

# 1-D plot example

plt.hist(ht)
plt.show()

# 1-D plot example

plt.hist(met)
plt.show()

# Hexbin 2D plot example

fig, ax = plt.subplots(ncols=1)
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
hb = ax.hexbin(nrjets, ngjets, gridsize=50, cmap='YlGn')
ax.set_title("Hexagon binned NRecoJets vs NGenJets")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')
plt.show()

# Simple 2-D scatter plot example

plt.scatter(ht, met)
plt.show()

# Simple 2-D histogram plot example

plt.hist2d(ht, met)
plt.show()

