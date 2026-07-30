import psutil
import os

def ProcInfo(process_name):
    Running = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["name", "pid", "username"])
        if(info["name"] == process_name):
            Running.append(info)
    return Running
    

def main():
    Ret = ProcInfo("Code.exe")
    print(Ret)

if __name__ == "__main__":
    main()