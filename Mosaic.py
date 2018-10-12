import numpy as np


Filename = input('What is the filename?');

try:
    readFile = open(Filename + '.csv','r');
    FileOpen = 1;
except:
    print("Error:\n File: " + Filename +'.csv'+ " does not exist.");
    FileOpen = 0;







# Create empty arrays for later use
Row = [];
List = [];
i = 0;

# Only run if the file exists and opens
if FileOpen:
    
    Merge = input('List tracks which are desired with disconnected tracks seperated by spaces and particles seperated by commas');

    AllTracks = Merge.split(',');
    AllTrackCount = len(AllTracks);

    PartTracks = Merge.replace(' ',',');
    PartTracks = PartTracks.split(',');
    PartTrackCount = len(PartTracks);
    
    MasterTracks = [];
    for i in AllTracks:
        MasterTracks.append(i[0]);
    MasterTracks = list(map(int,MasterTracks));

    TotalLength = 5;

    for line in readFile:
        TotalLength += 1;

        Split = line.split(',');
    
        if i:
            if Split[0] in PartTracks:
                for j in AllTracks:
                    if Split[0] in j.split(' '):
                        Split[0] = j[0];
                        break;

                Row = (int(Split[0]), int(Split[1]), float(Split[2]), float(Split[3]));
                List.append(Row);  
        
        # Skip header
        else:
            i = i+1;
        
    readFile.close();


    for i in MasterTracks:
        DataStructureX =[[] for i in range(TotalLength)];
        DataStructureY =[[] for i in range(TotalLength)];
        for Row1 in List:
            for Row2 in List:
                if (Row1[0] == i and Row2[0] == i and Row2[1]>Row1[1]):
                    FrameSeperation = Row2[1]-Row1[1];

                    SqDiffX= (Row1[2]-Row2[2])**2;
                    DataStructureX[FrameSeperation].append(SqDiffX);
                    SqDiffY= (Row1[3]-Row2[3])**2;
                    DataStructureY[FrameSeperation].append(SqDiffY);


        FilenameOut = Filename + '_MSD_Track_'+str(i) + '.csv';     
        Output=open(FilenameOut,'w');
        Output.write('Frame,SqXDiff,SqYDiff\n'); 
  
        for k in range(len(DataStructureX)):
            if DataStructureX[k] != []:
                meanX = np.nanmean(DataStructureX[k]);
                meanY = np.nanmean(DataStructureY[k]);

                Output.write(str(k) +','+ str(meanX) +','+ str(meanY)+'\n');

          
    print('Finished\n')

