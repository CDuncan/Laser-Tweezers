import numpy as np
import findDetails as FD
import pandas as pd
from scipy import stats

def errorCalc(Readings,**kwargs):
    pcErr = kwargs.get('pcErr', None)
    listErr = kwargs.get('listErr', None)
    WMean, eWMean = 0 , 0
    if pcErr != None:
        w = [(pcErr*x)**-2 for x in Readings]
        Num = 0
        Den = 0
        for i in range(len(Readings)):
            Num += w[i]*Readings[i]
            Den += w[i]
        WMean = Num/Den
        eWMean = 1/np.sqrt(Den)

    if not listErr.empty:
        w = listErr**-2
        Num = 0
        Den = 0
        for i in range(len(Readings)):
            Num += w[i]*Readings[i]
            Den += w[i]
        WMean = Num/Den
        eWMean = 1/np.sqrt(Den)




    return WMean, eWMean