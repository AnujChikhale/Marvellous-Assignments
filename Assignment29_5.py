import os
import sys

filename = sys.argv[1]
string = sys.argv[2]
count= 0
for FolderName, SubFolder, FileName in os.walk("Marvellous"):
    for file in FileName:
        if(file == filename ):
            filepath1 = os.path.join(FolderName,filename)
            fobj1 = open(filepath1, "r")
            for line in fobj1:
                data = line.split()
                for word in data:
                    if(word == string):
                        count = count+1       



print(count)