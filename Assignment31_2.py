import schedule

def DisplayMessage(str):
    print(str)

def main():
    message = input("Enter the message: ")
    schedule.every(5).seconds.do(DisplayMessage,message)
    while True:
        schedule.run_pending()
    
if __name__ == "__main__":
    main()