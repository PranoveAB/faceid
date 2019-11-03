import yagmail

receiver = "pranove.ab@gmail.com"  # receiver email address
body = "Attendance File"  # email body
filename = "./Attendance/Attendance_2019-09-21_15-55-52.csv"  # attach the file

# mail information
yag = yagmail.SMTP("1.zoomind@gmail.com", "pranove2")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
