import schedule
import datetime
import time

def CurrTime():
    current = datetime.datetime.now()
    print("CUrrent time is: ", current)

def main():

    schedule.every(1).minute.do(CurrTime)
    while(True):
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()