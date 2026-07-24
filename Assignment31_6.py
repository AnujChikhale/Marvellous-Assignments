import schedule
import datetime
import time

def w1():
    print("Start your weekly goals")

def w2():
    print("Review your weekly progress")

def w3():
    print("weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(w1)
    schedule.every().wednesday.at("17:00").do(w2)
    schedule.every().friday.at("18:00").do(w3)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()