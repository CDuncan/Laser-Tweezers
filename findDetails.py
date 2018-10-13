import pandas as pd

def findDetails(FileName):
    DataLoc = 'Measurements.csv'
    Data = pd.read_csv(DataLoc,header=0,index_col=0)
    Details = Data.loc[FileName]
    return Details

def findScale(FileName):
    MassData = findDetails(FileName)
    LensLoc = 'Scales.csv'
    Data = pd.read_csv(LensLoc,header=0,index_col=0)
    Details = float(Data.loc[MassData[3]])
    return Details




