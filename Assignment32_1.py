import schedule
import datetime
import time

def Create_file():
    filename = "File%s.txt"%datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = filename.replace(" ", "_")
    filename = filename.replace("-", "_")
    filename = filename.replace(":", "_")
    fobj = open(filename, "w")
    fobj.write(f"File name is {filename}\n")
    fobj.write(f"Current Date is : {datetime.datetime.now().date()}\n")
    fobj.write(f"Current time is: {datetime.datetime.now().time()}")
    print(f"{filename} created successfully")

def main():
    schedule.every(1).minute.do(Create_file)
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()