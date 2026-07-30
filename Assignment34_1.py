import psutil
import os

def ProcInfo():
    ProcessList = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["name", "pid", "username"])
        ProcessList.append(info)
    return ProcessList

def main():
    Ret = ProcInfo()
    print(Ret)

if __name__ == "__main__":
    main()