

import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

def SendMail(receiver_email, logfile):
    try:
        sender_email = "chikhaleanuj38@gmail.com"
        sender_password = "GOOGLE_APP_PASSWORD"

        msg = EmailMessage()

        msg["Subject"] = "Plateform Survillence Report"
        msg["From"] = sender_email
        msg["to"] = receiver_email
        msg.set_content("Please find the duplicate files report attached")
        f = open(logfile,"rb")
        file_data = f.read()
        msg.add_attachment(
            file_data,
            maintype="text",
            subtype="plain",
            filename = logfile
        )
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
        smtp.quit()
        f.close()
        return True
    except Exception as e:
        print(e)
        return False


def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name", "username", "status"])
        info["CPU_percent"] = proc.cpu_percent(None)
        info["Memory_percent"] = proc.memory_percent()

        listprocess.append(info)
    return listprocess

def Plateform_Survillence(FolderName, receiver_email):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Enable to process as folder name is existing but its not a Directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for logfile gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log"%timestamp)
    fobj = open(FileName, "w")

    print(f"Log files gets successfully created with name: {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Plateform Survillence system ----\n")
    fobj.write("Log file gets created at: "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("---------- System Report ----------\n")

    #CPU Information
    fobj.write("Number of active CPU cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    #RAM Information
    memory = psutil.virtual_memory()
    fobj.write("RAM usage : %s\n" %memory.percent)
    fobj.write("Total RAM available : %s \n" %memory.total)

    fobj.write(Border+"\n")

    #Network usage
    netobj = psutil.net_io_counters()
    fobj.write("Network usage report\n")
    fobj.write("Sent: %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Recieve: %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    #Process Log
    Data = ProcessScan()
    for info in Data:
        #fobj.write(f"{info} \n")
        fobj.write("PID: %s\n"%info.get("pid"))
        fobj.write("Name: %s\n"%info.get("name"))
        fobj.write("UserName: %s\n"%info.get("username"))
        fobj.write("Status: %s\n"%info.get("status"))
        fobj.write("CPU usage: %.2f\n"%info.get("CPU_percent"))
        fobj.write("RAM usage: %2f\n"%info.get("Memory_percent"))
        

        fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("---------- End of Log file ---------\n")
    fobj.write(Border+"\n")

    email_send = SendMail(receiver_email, FileName)
    if(email_send == True):
        fobj.write(f"Email sent successfully to {receiver_email}")
    else:
        fobj.write("Error to send email")

    fobj.close()



def main():
    Border = "-"*50
    print(Border)
    print("----- Marvellous Plateform Survillence system ----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to perform ")
            print("1 : It fetch the information of running processes")
            print("2 : It fetch the information about primary storage as RAM")
            print("3 : It fetch the information about secondary storage as HDD")
            print("4 : It fetch the information about microprocessor")
            print("5 : It gets autoschedulled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically") 
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as: ")
            print(f"python {sys.argv[0]} Time_interval Folder_Name")
            print("Time_interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for log file creation")
        else:
            print("Enable to proceed as arguments are not matching")
            print("Please use --h or --u for getting more details")

    #Actual Project code
    elif(len(sys.argv) == 4):
        print("Schedular started sucessfully")
        print("Press ctrl+c to abort the automation script")
        schedule.every(int(sys.argv[1])).minutes.do(Plateform_Survillence, sys.argv[2], sys.argv[3])
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Enable to proceed as arguments are not matching")
        print("Please use --h or --u for getting more details")

    print(Border)
    print(" Thank you for using Marvellous Survillence system ")
    print(Border)

if __name__ == "__main__":
    main()