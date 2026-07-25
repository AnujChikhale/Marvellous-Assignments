import schedule
import datetime
import time
import os
import sys

def FileSize(filename, Directory_path):
    fobj = open("FileSizeLog.txt", "a+")
    for FolderName, SubFolder, FileName in os.walk(Directory_path):
        for files in FileName:
            if(files == filename):
                filepath = os.path.join(FolderName,filename)
                fobj.write(f"File path: {os.path.abspath(filename)}\n")
                fobj.write(f"File size: {os.path.getsize(filepath)} bytes\n")
                fobj.write(f"Date and time: {datetime.datetime.now()}\n")

def main():
    schedule.every(30).seconds.do(FileSize, sys.argv[1], sys.argv[2])
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()