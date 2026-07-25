import schedule
import datetime
import time
import os
import sys

def Display(Directory_name, File_name):
    for FolderName, SubFolder, Filename in os.walk(Directory_name):
        found = False
        for files in Filename:
            if(files == File_name):
                found = True
                filepath= os.path.join(FolderName,files)
                fobj = open(filepath, "r")
                for lines in fobj:
                    print(lines)
        if(found == False):
            print("File Does not exist in current directory")
                
def main():
    schedule.every(1).minute.do(Display, sys.argv[1],sys.argv[2])
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()