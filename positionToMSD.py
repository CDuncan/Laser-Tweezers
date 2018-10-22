import glob
import numpy as np
import findDetails as FD




Hold = glob.glob("Raw/Positions/*.csv")
for file in Hold:
    StrippedFile, arrayValX, arrayValY = FD.findPositions(file)
    
    OutFile = "Export/MSD/" + StrippedFile + '.csv'
    Output = open(OutFile,'w')
    Output.write('Frame Diff,MSD x,MSD y\n')


    Length = len(arrayValX)
    for i in range(1,Length):
        SumX = 0
        SumY = 0
        Count = 0
        for j in range(0,Length-i):
            SumX += (arrayValX[j+i]-arrayValX[j])**2
            SumY += (arrayValY[j+i]-arrayValY[j])**2
            Count +=1
        MeanX = SumX/Count
        MeanY = SumY/Count
        
        Output.write(str(i) +','+ str(MeanX) +','+ str(MeanY) +'\n')
        print(' File: ' + str(StrippedFile) + '  ',end='\r')
