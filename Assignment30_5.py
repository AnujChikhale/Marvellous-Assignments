import time
import datetime
import schedule

def task():
    fobj = open("Marvellous.txt", "a")
    fobj.write("Task executed at: "+str(datetime.datetime.now())+ "\n")

def main():
    schedule.every(15).seconds.do(task)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

