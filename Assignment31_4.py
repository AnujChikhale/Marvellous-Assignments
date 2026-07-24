import sys
import datetime
import time
import schedule

def Create_log_File():
    Log_file_name = "Marvellous%s.log"%(datetime.datetime.now())
    Log_file_name = Log_file_name.replace(" ","_")
    Log_file_name = Log_file_name.replace(":","_")

    fobj = open(Log_file_name, "w")

    fobj.write("Log file created successfully \n")
    fobj.write(f"Creation time: {time.ctime()}")

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to create log file every 10 mins")
            print("For better usage check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the file as :")
            print("python file_name.py")
    elif(len(sys.argv) == 1):
        schedule.every(10).seconds.do(Create_log_File)
        while True:
            schedule.run_pending()
            time.sleep(10)
    else:
        print("Invalid number of arguments passed")

if __name__ == "__main__":
    main()