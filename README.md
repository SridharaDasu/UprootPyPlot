
Installation:

```
git clone https://github.com/SridharaDasu/UprootPyPlot.git
cd UprootPyPlot
virtualenv --python python3 venv
pip3 install -r requirements.txt
export UprootPyPlot=$PWD
```

Data:

Obtain a Delphes root file from: https://pages.hep.wisc.edu/~dasu/physics535-data
for example:

```
curl https://pages.hep.wisc.edu/~dasu/physics535-data/e+e-ZH/Events/run_01/tag_1_delphes_events.root
mv tag_1_delphes_events.root e+e-ZH.root
```

Usage:

```
cd $UprootPyPlot
source venv/bin/activate
python test_plots.py e+e-ZH.root
```

Activity:

Copy test_plots.py to your own python file and make the plots that interest you.
