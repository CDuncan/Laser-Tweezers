import glob
import numpy as np
import scipy.stats as sp
import findDetails as FD
import seaborn as sb
import matplotlib.pyplot as plt


line = []
kBT = (273+21)*1.38064852E-23
Hold = glob.glob("Raw/*.csv")

File = 'Data/PositionDistribution.csv'
Output = open(File,'w')
Output.write('Filename,Stiffness x, Sku x, Stiffness y, Sku y\n')


for file in Hold:
    StrippedFile, arrayValX, arrayValY = FD.findPositions(file)

    #ax = sb.jointplot(x=arrayValX,y=arrayValY,kind="hex")
    ax = sb.jointplot(x=arrayValX,y=arrayValY,kind="kde")
    plt.show()

    SpringX = kBT/(np.nanvar(arrayValX))
    KurtX = sp.kurtosis(arrayValX)
    SpringY = kBT/(np.nanvar(arrayValY))
    KurtY = sp.kurtosis(arrayValY)

    
    Output.write(StrippedFile +','+ str(SpringX) +','+ str(KurtX) + ',' + str(SpringY)+','+ str(KurtY)+'\n')