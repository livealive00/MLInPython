# -*- coding: utf-8 -*-

import pylab
import scipy.stats as stats
import urllib2

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases"
              "/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib2.urlopen(target_url)

xList = []
labels = []

for line in data:
    row = line.strip().split(",")
    xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

# 세번째 컬럼의 통계량 생성
col = 3
colData = []

colData = []
for row in xList:
    colData.append(float(row[col]))

stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()