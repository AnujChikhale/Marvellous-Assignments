import schedule
import datetime
import time

def task1():
    print("Lunchtime!")
def task2():
    print("Wrap up")

def main():
    schedule.every().day.at("13:00").do(task1)
    schedule.every().day.at("18:00").do(task2)

    while True:
        schedule.run_pending()
        time.sleep(1000)

if __name__ == "__main__":
    main()
