Installation:

```
git clone 
virtualenv --python python3 venv
pip install -r requirements.txt
```

Data:

Obtain a Delphes root file from: https://pages.hep.wisc.edu/~dasu/physics535-data
Example root file: https://pages.hep.wisc.edu/~dasu/physics535-data/e+e-ZH/Events/run_01/tag_1_delphes_events.root

Usage:

```
source venv/bin/activate
python test_plots.py <delphes_root_file>
```

Activity:

Copy test_plots.py to your own python file and make the plots that interest you.
