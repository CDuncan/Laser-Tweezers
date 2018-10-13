import glob
import numpy as np
import scipy.stats as sp
import findDetails as FD

line = []
kBT = (273+21)*1.38064852E-23
Hold = glob.glob("Raw/*.csv")

File = 'Data/PositionDistribution.csv'
Output = open(File,'w')
Output.write('Filename,Stiffness x, Sku x, Stiffness y, Sku y\n')


for file in Hold:
    readFile = open(file,'r')
    valX = []
    valY = []
    for line in readFile:
        Split = line.split(',')
        valX.append(float(Split[1]))
        valY.append(float(Split[2]))

    StrippedFile = file[4:]
    StrippedFile = StrippedFile[:-4]
    ScaleFactor = FD.findScale(StrippedFile)

    arrayValX = np.asarray(valX)*ScaleFactor
    arrayValY = np.asarray(valY)*ScaleFactor


    SpringX = kBT/(np.nanvar(arrayValX))
    KurtX = sp.kurtosis(arrayValX)
    SpringY = kBT/(np.nanvar(arrayValY))
    KurtY = sp.kurtosis(arrayValY)

    
    Output.write(StrippedFile +','+ str(SpringX) +','+ str(KurtX) + ',' + str(SpringY)+','+ str(KurtY)+'\n')