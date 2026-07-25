import schedule
import time
import os
import datetime
import sys

def Delete_Empty_Files(Directory_name):
    count = 0
    for FolderName, SubFolder, FileName in os.walk(Directory_name):
        for file in FileName:
            filepath = os.path.join(FolderName,file)
            if(os.path.getsize(filepath) == 0):
                fobj = open("Deleted_empty_log.txt", "a+")
                fobj.write(f"{file} at {filepath} deleted at {datetime.datetime.now()}\n")
                os.remove(filepath) #this is used to delete any file permanently
                count = count+1
                print(f"{file} deleted successfully")
                
    if(count == 0):
        print("No empty file found")

def main():
    schedule.every(20).seconds.do(Delete_Empty_Files, sys.argv[1])
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()