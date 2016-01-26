# -*- coding: utf-8 -*-

import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot
from math import exp

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
              "/abalone/abalone.data")

abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'While weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

corMat = DataFrame(abalone.iloc[:, 1:9].corr())
print(corMat)

plot.pcolor(corMat)
plot.show()