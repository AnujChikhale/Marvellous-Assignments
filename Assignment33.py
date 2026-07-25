import schedule
import datetime
import sys
import time
import os
import hashlib
import smtplib
from email.message import EmailMessage

def SendMail(receiver_email, logfile):
    try:
        sender_email = "chikhaleanuj38@gmail.com"
        sender_password = "tcoi vceb eaot ypxh"

        msg = EmailMessage()

        msg["Subject"] = "Duplicate files report"
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

def CalculateCheckSum(Directory_path,receiver_email):
    hashcodes = []
    counter = 0
    duplicateFiles = 0
    duplicateFilesDeleted = 0
    duplicateFilesPath = []
    checkSumValues = []
    for FolderName, SubFolder, FileName in os.walk(Directory_path):
        start_time = time.perf_counter()
        for file in FileName:
            counter = counter+1
            filepath = os.path.join(FolderName, file)
            fobj = open(filepath,"rb")
            
            hobj = hashlib.md5()
        
            Buffer = fobj.read(1000)
        
            while(len(Buffer) > 0):
                hobj.update(Buffer)
                Buffer = fobj.read(1000)
        
            fobj.close()
            curr_hash = hobj.hexdigest()
            duplicate = False
            for hash in hashcodes:
                if(curr_hash == hash):
                    duplicate = True
                    duplicateFiles = duplicateFiles+2
                    duplicateFilesPath.append(os.path.abspath(filepath))
                    checkSumValues.append(curr_hash)
            if(duplicate == True):
                os.remove(filepath)
                duplicateFilesDeleted = duplicateFilesDeleted + 1
            else:
                hashcodes.append(hobj.hexdigest())

    end_time = time.perf_counter()
    filename = "DuplicateRemovalLog_%s.txt"%datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = filename.replace(" ", "_")
    filename = filename.replace(":","_")
    lobj = open(filename, "w")
    lobj.write(f"Starting time of Directory Scanning: {start_time}\n")
    lobj.write(f"Completion time of Directory Scanning: {end_time}\n")
    lobj.write(f"Name of Directory Scanned: {Directory_path}\n")
    lobj.write(f"Total Number of files scanned: {counter}\n")
    lobj.write(f"Total Number of duplicate files scanned: {duplicateFiles}\n")
    lobj.write(f"Total Number of duplicate files deleted: {duplicateFilesDeleted}\n")
    lobj.write(f"Complete path of duplicate files deleted: {duplicateFilesPath}\n")
    lobj.write(f"Checksum values of duplicate files: {checkSumValues}\n")
    email_send = SendMail(receiver_email, filename)
    if(email_send == True):
        lobj.write(f"Email sent successfully to {receiver_email}")
    else:
        lobj.write("Error to send email")
    lobj.close()


def main():
    schedule.every(10).seconds.do(CalculateCheckSum, sys.argv[1], sys.argv[2])
    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()