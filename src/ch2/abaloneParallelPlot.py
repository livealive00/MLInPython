# -*- coding: utf-8 -*-

import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot
from math import exp

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
              "/abalone/abalone.data")

abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'While weight', 'SHucked weight', 'Viscera weight', 'Shell weight', 'Rings']

summary = abalone.describe()
minRings = summary.iloc[3,7]
maxRings = summary.iloc[7,7]
nrows = len(abalone.index)

for i in range(nrows):
    dataRow = abalone.iloc[i, 1:8]
    labelColor = (abalone.iloc[i,8] - minRings) / (maxRings - minRings)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()

## 평균과 표준편차로 다시 정규화, 이후 로짓 함수로 압축
meanRings = summary.iloc[1,7]
sdRings = summary.iloc[2,7]

for i in range(nrows):
    dataRow = abalone.iloc[i,1:8]
    normTarget = (abalone.iloc[i,8]-minRings) /sdRings
    labelColor = 1.0/(1.0+exp(-normTarget))
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()