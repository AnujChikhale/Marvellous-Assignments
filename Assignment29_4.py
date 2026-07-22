import os

filename1 = input("Enter file1 name: ")
filename2 = input("Enter file2 name: ")
data1 = ""
data2 = ""
result = False
for FolderName, SubFolder, FileName in os.walk("Marvellous"):
    for file in FileName:
        if(file == filename1 or file == filename2):
            filepath1 = os.path.join("Marvellous",filename1)
            fobj1 = open(filepath1, "r")
            data1 = fobj1.read()
            filepath2 = os.path.join("Marvellous",filename2)
            fobj2 = open(filepath2, "r")
            data2 = fobj2.read()

    
        else:
            print("File you entered not found!")
if(data1==data2):
    print("SUCCESS")
else:
    print("Failure")

