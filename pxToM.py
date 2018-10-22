import numpy as np
import pandas as pd
import errorCalc as eC




Data = pd.read_csv('Repo/Scales.csv',header=0,index_col=0)
listErr = [];   listMean = []

ReadingsAir = pd.read_csv('Calibration/CB_0.csv',header=0,index_col=None)
ReadingsAir['Distance'] = ReadingsAir['Lines']*10e-6
ReadingsAir['DistancePcErr'] = ReadingsAir['Lines'] -ReadingsAir['Lines'] +0.1
ReadingsAir['PixelsPcErr'] = 15/ReadingsAir['Pixels']
ReadingsAir['DistPerPx'] = ReadingsAir['Distance']/ReadingsAir['Pixels']
ReadingsAir['DistPerPxErr'] = ReadingsAir['DistPerPx']*np.sqrt((ReadingsAir['DistancePcErr'])**2 + (ReadingsAir['PixelsPcErr'])**2)
meanAir,errMeanAir = eC.errorCalc(ReadingsAir['DistPerPx'],listErr = ReadingsAir['DistPerPxErr'])
listMean.append(meanAir);   listErr.append(errMeanAir)

ReadingsOil = pd.read_csv('Calibration/CB_1.csv',header=0,index_col=None)
ReadingsOil['Distance'] = ReadingsOil['Lines']*10e-6
ReadingsOil['DistancePcErr'] = ReadingsOil['Lines'] -ReadingsOil['Lines'] +0.1
ReadingsOil['PixelsPcErr'] = 15/ReadingsOil['Pixels']
ReadingsOil['DistPerPx'] = ReadingsOil['Distance']/ReadingsOil['Pixels']
ReadingsOil['DistPerPxErr'] = ReadingsOil['DistPerPx']*np.sqrt((ReadingsOil['DistancePcErr'])**2 + (ReadingsOil['PixelsPcErr'])**2)
meanOil,errMeanOil = eC.errorCalc(ReadingsOil['DistPerPx'],listErr = ReadingsOil['DistPerPxErr'])
listMean.append(meanOil);   listErr.append(errMeanOil)

Data['Scale Factor']=listMean
Data['Scale Factor Error']=listErr
Data.to_csv('Repo/Scales.csv')