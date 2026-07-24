import schedule

def Message(str):
    print(str)

def main():
    message = input("Enter the message: ")
    time_interval = int(input("Enter the time interval: "))
    if(time_interval > 0):
        schedule.every(time_interval).seconds.do(Message,message)
        while True:
            schedule.run_pending()
    else:
        print("Interval should be positive number")

if __name__ == "__main__":
    main()