import pandas as pd
import numpy as np
import os

def findFileName(DataSet):
    StrippedFile = os.path.splitext(os.path.basename(DataSet))[0]
    return StrippedFile

def findDetails(DataSet):
    DataLoc = 'Repo' + '/' + 'Measurements.csv'
    Data = pd.read_csv(DataLoc,header=0,index_col=0)
    Details = Data.loc[DataSet]
    return Details

def findScale(DataSet):
    fullData = findDetails(DataSet)
    LensLoc = 'Repo' + '/' + 'Scales.csv'
    Data = pd.read_csv(LensLoc,header=0,index_col=0)
    ScaleFactor = float(Data.loc[fullData[3]])
    return ScaleFactor

def findDensity(DataSet):
    fullData = findDetails(DataSet)
    DensLoc = 'Repo' + '/' + 'Densities.csv'
    Data = pd.read_csv(DensLoc,header=0,index_col=0)
    Density = float(Data.loc[fullData[0]])
    return Density


def findPositions(DataSet):
    readFile = open(DataSet,'r')
    valX = []
    valY = []

    for line in readFile:
        Split = line.split(',')
        valX.append(float(Split[1]))
        valY.append(float(Split[2]))

    StrippedFile = findFileName(DataSet)
    ScaleFactor = findScale(StrippedFile)

    arrayValX = np.asarray(valX)*ScaleFactor
    arrayValY = np.asarray(valY)*ScaleFactor

    return StrippedFile, arrayValX, arrayValY

