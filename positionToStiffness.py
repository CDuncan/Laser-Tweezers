import glob
import numpy as np
import scipy.stats as sp
import findDetails as FD
import seaborn as sb
import matplotlib.pyplot as plt


kBT = (273+21)*1.38064852E-23
Hold = glob.glob("Raw/*.csv")

OutputFilename = 'Data/PositionDistribution.csv'
Output = open(OutputFilename,'w')
Output.write('Filename,Stiffness x, Sku x, Stiffness y, Sku y\n')


for file in Hold:
    StrippedFile, arrayValX, arrayValY = FD.findPositions(file)

    StrippedFile = file[4:]
    StrippedFile = StrippedFile[:-4]
    Details = FD.findDetails(StrippedFile)
    #ax = sb.jointplot(x=arrayValX,y=arrayValY,kind="hex")
    arrayValX *= 1e6;
    arrayValY *= 1e6;

    CentreX = np.median(arrayValX)
    CentreY = np.median(arrayValY)

    LabelX = 'x position ($um$)'
    LabelY = 'y position ($um$)'
    LabelTitle = "Position density for " + str(Details[1]) +"$um$ " + str(Details[0]) + " beads. " + str(Details[4]) + " motion."
    ax = sb.jointplot(x=arrayValX,y=arrayValY,kind="kde",xlim=[CentreX-0.15,CentreX+0.15],ylim=[CentreY-0.15,CentreY+0.15])
    ax.set_axis_labels(xlabel=LabelX,ylabel=LabelY)
    ax.fig.suptitle(LabelTitle)
    ax.fig.subplots_adjust(top=0.9)
    ax.savefig("Figures\\Position\\" + StrippedFile+".png")

    #plt.show()

    SpringX = kBT/(np.nanvar(arrayValX))
    KurtX = sp.kurtosis(arrayValX)
    SpringY = kBT/(np.nanvar(arrayValY))
    KurtY = sp.kurtosis(arrayValY)

    
    Output.write(StrippedFile +','+ str(SpringX) +','+ str(KurtX) + ',' + str(SpringY)+','+ str(KurtY)+'\n')