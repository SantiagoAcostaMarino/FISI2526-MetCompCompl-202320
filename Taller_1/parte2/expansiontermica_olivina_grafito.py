
import numpy as np
import matplotlib.pyplot as plt

from expansiontermicamineral import ExpansionTermicaMineral

Graphite_A=ExpansionTermicaMineral("graphite_mceligot_2016.csv")
Graphite=ExpansionTermicaMineral.alpha(Graphite_A)
Graphite

Olivine=ExpansionTermicaMineral("olivine_angel_2017.csv")
Olivine=ExpansionTermicaMineral.alpha(Olivine)
Olivine