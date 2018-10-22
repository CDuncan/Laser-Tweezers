import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import findDetails as FD

Filename = input('What is the filename?')
Directory = 'Export/MSD/' + Filename + '.csv'

try:
    Data = pd.read_csv(Directory,header=0,index_col=False)
    Details = FD.findDetails(Filename)

    Data.loc[:,'Frame Diff']/= Details[5]
    Data.rename(columns={'Frame Diff': 'Time (seconds)'}, inplace=True)
    Data.set_index('Time (seconds)', inplace=True)


    FileOpen = 1


except:
    print("Error:\n File: " + Filename +'.csv'+ " does not exist.")
    FileOpen = 0


if FileOpen:

    sb.set(style="ticks")
    sb.set_style("darkgrid", {"axes.facecolor": ".9"})
    ax = sb.lineplot(data=Data)


    LabelX = 'Time ($s$)'
    LabelY = 'MSD ($m^2$)'
    LabelTitle = "MSD vs time for " + str(Details[1]) +"$um$ " + str(Details[0]) + " beads. " + str(Details[4]) + " motion at " + str(Details[5]) +" FPS"
    ax.set(xlabel=LabelX, ylabel=LabelY, xlim=(0,None)) 
    #ax.set(yscale="log")
    ttl = ax.title
    ttl.set_position([.5, 1.05])


    plt.show()

    #fig = ax.get_figure()
    #fig.savefig("Export/Figures/MSD/" + Filename + ".png")