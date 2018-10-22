import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import findDetails as FD
import glob
from scipy import optimize

#Filename = input('What is the filename?')
#Directory = 'Export/MSD/' + Filename + '.csv'

Hold = glob.glob("Export/MSD/*.csv")

OutputFilename = 'Export/MSDFlat.csv'
Output = open(OutputFilename,'w')
Output.write('Filename,Power,Stiffness x,Stiffness y\n')


for file in Hold:

    try:
        StrippedFile = file[11:]
        StrippedFile = StrippedFile[:-4]

        Data = pd.read_csv(file,header=0,index_col=False)
        Details = FD.findDetails(StrippedFile)
        Data = Data.truncate(before=0,after=len(Data)*0.8)


        Data.loc[:,'Frame Diff']/= Details[5]
        Data.rename(columns={'Frame Diff': 'Time (seconds)'}, inplace=True)
        Data.set_index('Time (seconds)', inplace=True)


        FileOpen = 1

    except:
        print("Error:\n File: " + file +'.csv'+ " does not exist.")
        FileOpen = 0



    if FileOpen:

        sb.set(style="ticks")
        sb.set_style("darkgrid", {"axes.facecolor": ".9"})
        ax = sb.lineplot(data=Data)


        LabelX = 'Time ($s$)'
        LabelY = 'MSD ($m^2$)'
        LabelTitle = "MSD vs time for " + str(Details[1]) +"$um$ " + str(Details[0]) + " beads. " + str(Details[4]) + " motion at " + str(Details[5]) +" FPS"
        ax.set(xlabel=LabelX, ylabel=LabelY, xlim=(0,None),title=LabelTitle) 
        #ax.set(yscale="log")
        ttl = ax.title
        ttl.set_position([.5, 1.05])

        time = Data.index.tolist()
        xData = Data["MSD x"].tolist()
        yData = Data["MSD y"].tolist()


        def test_func(x,a):
            return a
        params, params_covariance = optimize.curve_fit(test_func, time, xData, p0=[1e-15])
        params2, params_covariance2 = optimize.curve_fit(test_func, time, yData, p0=[1e-15])


        if (str(Details[4]) == "Trapped"):
            Output.write(StrippedFile +','+ str(Details[7]) +','+ str(params[0]) + ',' + str(params2[0])+ '\n')

        #plt.show()

        fig = ax.get_figure()
        fig.savefig("Export/Figures/MSD/" + StrippedFile + ".png")
        plt.close(fig='all')
        print(' File: ' + str(StrippedFile) + '  ',end='\r')
print("Done :)")
