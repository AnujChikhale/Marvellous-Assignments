import os
import datetime
import time
import schedule

def Scanner():
    Number_of_files = 0
    Number_of_subdirectories = 0
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        print("Directory Name: ",FolderName)
        for files in FileName:
            Number_of_files = Number_of_files+1
        for subdirectories in SubFolder:
            Number_of_subdirectories = Number_of_subdirectories+1
    print("Number of files: ",Number_of_files)
    print("Number of subdirectories: ",Number_of_subdirectories)
    print("Date and timing of scanning: ",datetime.datetime.now())

def main():
    schedule.every(1).minute.do(Scanner)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
