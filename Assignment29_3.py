import os

filename = input("Enter file name: ")
result = False
dobj = open("Demo.txt", "w")
for FolderName, SubFolder, FileName in os.walk("Marvellous"):
    for file in FileName:
        if(file == filename):
            result = True
    if(result == True):
        filepath = os.path.join("Marvellous",filename)
        fobj = open(filepath, "r")
        data = fobj.read()
        dobj.write(data)    
        fobj.close()  
    else:
        print("File you entered not found!")

