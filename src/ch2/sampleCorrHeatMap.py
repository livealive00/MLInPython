# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plot
from pandas import DataFrame


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
              "/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

corMat = DataFrame(rocksVMines.corr())
plot.pcolor(corMat)
plot.show()
