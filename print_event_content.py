import sys
import uproot

if len(sys.argv) == 2:
    input_file = sys.argv[1]
else:
    input_file = "c3-zh-aa-bbtautau.root"

input = uproot.open(input_file)

tree = input["Delphes;1"]

print(f"Content of the file {input_file}")
print('The content of the tree = input["Delphes;1"] is:')

for item in tree.items():
    print(item[0])

print('You can access the elements as array = tree["Particle"]["Particle.E"].array()')
print("You may want to use np.squeeze(array)")
