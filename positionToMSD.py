import glob
import numpy as np
import scipy.stats as sp
import findDetails as FD


line = []


Hold = glob.glob("Raw/*.csv")
for file in Hold:
    readFile = open(file,'r');
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
    
    OutFile = "Data" + file[3:]
    Output = open(OutFile,'w')
    Output.write('Frame Diff,MSD x,MSD y\n')


    Length = len(arrayValX)
    for i in range(1,Length):
        SumX = 0;
        SumY = 0;
        Count = 0;
        for j in range(0,Length-i):
            SumX += (arrayValX[j+i]-arrayValX[j])**2
            SumY += (arrayValY[j+i]-arrayValY[j])**2
            Count +=1
        MeanX = SumX/Count
        MeanY = SumY/Count
        
        Output.write(str(i) +','+ str(MeanX) +','+ str(MeanY) +'\n')