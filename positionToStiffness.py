import glob
import numpy as np
import scipy.stats as sp
import findDetails as FD
import seaborn as sb
import matplotlib.pyplot as plt


kBT = (273+21)*1.38064852E-23
Hold = glob.glob("Raw/*.csv")

OutputFilename = 'Export/PositionDistribution.csv'
Output = open(OutputFilename,'w')
Output.write('Filename,Stiffness x, Sku x, Stiffness y, Sku y\n')


for file in Hold:
    StrippedFile, arrayValX, arrayValY = FD.findPositions(file)

    StrippedFile = file[4:]
    StrippedFile = StrippedFile[:-4]
    Details = FD.findDetails(StrippedFile)

    # Convert to micrometres and set centre of graph
    microArrayValX = (arrayValX-np.median(arrayValX))*1e6
    microArrayValY = (arrayValY-np.median(arrayValY))*1e6

    # Calculate 
    SpringX = kBT/(np.nanvar(arrayValX))
    KurtX = sp.kurtosis(arrayValX)
    SpringY = kBT/(np.nanvar(arrayValY))
    KurtY = sp.kurtosis(arrayValY)


    # Plot graph and export as png
    LabelX = 'x position ($um$)'
    LabelY = 'y position ($um$)'
    LabelTitle = "Position density for " + str(Details[1]) +"$um$ " + str(Details[0]) + " beads. " + str(Details[4]) + " motion."
    sb.set()
    graph = sb.jointplot(x=microArrayValX,y=microArrayValY,kind="kde",xlim=[-0.15,+0.15],ylim=[-0.15,+0.15],shade_lowest=False)
    graph.set_axis_labels(xlabel=LabelX,ylabel=LabelY)
    graph.fig.suptitle(LabelTitle)
    graph.fig.subplots_adjust(top=0.9)
    Data = [['%.2e' % SpringX, '%.2e' % SpringY],['%.2f' % KurtX, '%.2f' % KurtY]]
    cols = ['X','Y']
    rows = ['Spring','Kurtosis']

    graph.ax_joint.table(cellText=Data,loc="best",colLabels=cols,rowLabels=rows,cellLoc="right",clip_on=True,zorder=1000,colWidths=[0.25]*2)

    graph.savefig("Export/Figures/Position/" + StrippedFile+".png")

    # Calculate 
    SpringX = kBT/(np.nanvar(arrayValX))
    KurtX = sp.kurtosis(arrayValX)
    SpringY = kBT/(np.nanvar(arrayValY))
    KurtY = sp.kurtosis(arrayValY)

    
    Output.write(StrippedFile +','+ str(SpringX) +','+ str(KurtX) + ',' + str(SpringY)+','+ str(KurtY)+'\n')