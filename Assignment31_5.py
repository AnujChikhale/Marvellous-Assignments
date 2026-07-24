import schedule
import os
import sys
import time

def Count_Files(Directory_path):
    Count = 0
    for FolderName, SubFolder,FileName in os.walk(Directory_path):
        for file in FileName:
            Count = Count+1
    print("Path of current directory is: ",os.path.abspath(Directory_path))
    print(f"Count of files in {Directory_path} is: ",Count)

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This file shows number of files in current directory")
            print("For more details refer --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Execute file in following format")
            print("python file_name.py Directory_path")
        else:
            schedule.every(1).minute.do(Count_Files, sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(10)
    else:
        print("Invlaid number of arguments")

if __name__ == "__main__":
    main()