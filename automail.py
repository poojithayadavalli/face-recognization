import yagmail
import os

receiver = input("Enter gmail Id : ")  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2020-05-29_13-34-03.csv"  # attach the file
try:
    #yag = yagmail.SMTP("dineshab95679@gmail.com", "rithika.6363")
    yag=yagmail.SMTP("poojithareddyyadavalli@gmail.com","yadavalli99")
    yag.send(to=receiver,subject="Attendance Report",contents=body,attachments=filename)
    print("success")
except:
    print("error")
