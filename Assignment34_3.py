import psutil
import os
import time
import sys

def ProcInfo():
    ProcessList = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["name", "pid", "username"])
        ProcessList.append(info)
    return ProcessList


def LogFile(Directory_name):
    FileName = "Logfile_%s.log" %time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(Directory_name, FileName)

    fobj = open(FileName, "w")
    Data = ProcInfo()
    for info in Data:
        fobj.write("Name: %s\n"%info.get("name"))
        fobj.write("PID: %s\n"%info.get("pid"))
        fobj.write("UserName: %s\n\n\n"%info.get("username"))
    fobj.close()

def main():
    LogFile(sys.argv[1])
    print("Log file created successfully")

if __name__ == "__main__":
    main()

