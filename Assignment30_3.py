import schedule
import datetime
import time

def Remainder():
    print("Coding Kar...")

def main():

    schedule.every(30).minute.do(Remainder)
    while(True):
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()