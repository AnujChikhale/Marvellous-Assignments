import os

filename = input("Enter file name: ")
result = False
for FolderName, SubFolder, FileName in os.walk("Marvellous"):
    for file in FileName:
        if(file == filename):
            result = True
    if(result == True):
        fobj = open(filename, "r")
        data = fobj.read()
        print(data)
    else:
        print("File absent")

