# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plot
from random import uniform

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
              "/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

target = []
for i in range(len(rocksVMines)):
    if rocksVMines.iat[i, 60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

## 시각화 개선버전

target = []
for i in range(len(rocksVMines)):
    if rocksVMines.iat[i, 60] == "M":
        target.append(1.0 + uniform(-0.1,0.1))
    else:
        target.append(0.0 + uniform(-0.1,0.1))

dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha=0.5, s=120)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()