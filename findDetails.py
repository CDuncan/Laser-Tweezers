import pandas as pd
import numpy as np

def findDetails(FileName):
    DataLoc = 'Repo' + '/' + 'Measurements.csv'
    Data = pd.read_csv(DataLoc,header=0,index_col=0)
    Details = Data.loc[FileName]
    return Details

def findScale(FileName):
    fullData = findDetails(FileName)
    LensLoc = 'Repo' + '/' + 'Scales.csv'
    Data = pd.read_csv(LensLoc,header=0,index_col=0)
    ScaleFactor = float(Data.loc[fullData[3]])
    return ScaleFactor

def findDensity(FileName):
    fullData = findDetails(FileName)
    DensLoc = 'Repo' + '/' + 'Densities.csv'
    Data = pd.read_csv(DensLoc,header=0,index_col=0)
    Density = float(Data.loc[fullData[0]])
    return Density

def findPositions(FileName):
    readFile = open(FileName,'r')
    valX = []
    valY = []

    for line in readFile:
        Split = line.split(',')
        valX.append(float(Split[1]))
        valY.append(float(Split[2]))

    StrippedFile = FileName[14:]
    StrippedFile = StrippedFile[:-4]
    ScaleFactor = findScale(StrippedFile)

    arrayValX = np.asarray(valX)*ScaleFactor
    arrayValY = np.asarray(valY)*ScaleFactor

    return StrippedFile, arrayValX, arrayValY