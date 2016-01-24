# PyBPL
Bayesian Program Learning toolkit in Python

###Purpose
This project is intended to build BPL into highly reusable Python modules, for the purpose of expiermentation and eventual use in production systems. 

The idea is to encourage discussion and experimentation around BPL and BPL-inspired variants, and to explore this class of models in production settings.

Please see the [wiki](https://github.com/MaxwellRebo/PyBPL/wiki) for details.

###Dependencies
numpy
nose

Do:

```
pip install -r requirements.txt
```

###Testing

Do:
```
nosetests
```

###Original Repo & Paper
The original BPL Matlab repo is here: https://github.com/brendenlake/BPL

The original BPL paper can be found on Science:

[Lake, B. M., Salakhutdinov, R., and Tenenbaum, J. B. (2015). Human-level concept learning through probabilistic program induction](http://www.sciencemag.org/content/350/6266/1332.abstract). Science, 350(6266), 1332-1338.

###TODOs
-Base BPL class, with tests
-Base parser class (for learning primitives), with tests
-Data formatters (text, time series, etc)
-Helper methods and utility classes as needed
