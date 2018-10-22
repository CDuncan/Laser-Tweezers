import numpy as np
import findDetails as fD
import pandas as pd
import errorCalc as eC
import seaborn as sb
import matplotlib.pyplot as plt




Data = pd.read_csv('Repo/PowerMeasurement.csv',header=0,index_col=0)
Readings = pd.read_csv('Calibration/CB_2.csv',header=None,index_col=0)

listMean = []
listErr = []
for index, row in Readings.iterrows():
    mean, err = eC.errorCalc(row.tolist(),pcErr = 0.08)
    listMean.append(mean)
    listErr.append(err)

Data['Measured Power'] = listMean
Data['Measured Power Error'] = listErr
listCurr = Data['Current'].tolist()
Data.to_csv('Calibration/PowerMeasurement.csv')

plt.errorbar(data=Data,x = 'Current',y='Measured Power',yerr='Measured Power Error')

plt.show()