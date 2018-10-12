import glob
import numpy as np
import scipy.stats as sp

line = []
kBT = (273+21)*1.38064852E-23
Hold = glob.glob("Data/*.csv")

File = 'Output/PositionDistribution.csv'
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

    arrayValX = np.asarray(valX)*6.23689E-08
    arrayValY = np.asarray(valY)*6.23689E-08


    SpringX = kBT/(np.nanvar(arrayValX))
    KurtX = sp.kurtosis(arrayValX)
    SpringY = kBT/(np.nanvar(arrayValY))
    KurtY = sp.kurtosis(arrayValY)

    
    Output.write(file +','+ str(SpringX) +','+ str(KurtX) + ',' + str(SpringY)+','+ str(KurtY)+'\n')