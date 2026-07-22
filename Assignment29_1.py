import os


def main():
    result = False
    name = input("Enter the file name: ")
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        for file in FileName:
            if(file == name):
                result = True
    if(result == True):
        print("File present")
    else:
        print("File absent")


if __name__ == "__main__":
    main()