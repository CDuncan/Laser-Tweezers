import pandas as pd

def findDetails(FileName):
    DataLoc = 'Repo' + '\\' + 'Measurements.csv'
    Data = pd.read_csv(DataLoc,header=0,index_col=0)
    Details = Data.loc[FileName]
    return Details

def findScale(FileName):
    fullData = findDetails(FileName)
    LensLoc = 'Repo' + '\\' + 'Scales.csv'
    Data = pd.read_csv(LensLoc,header=0,index_col=0)
    ScaleFactor = float(Data.loc[fullData[3]])
    return ScaleFactor

def findDensity(FileName):
    fullData = findDetails(FileName)
    DensLoc = 'Repo' + '\\' + 'Densities.csv'
    Data = pd.read_csv(DensLoc,header=0,index_col=0)
    Density = float(Data.loc[fullData[0]])
    return Density


