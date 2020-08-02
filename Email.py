import smtplib

sender = 'ptiwari30@csc.com'
receivers = ['Vaibhav.Juneja@Xchanging.com']
Subject = " Python"
message = """from Python with Love
Regards,
PRADYUT TIWARI
Support Manager- Account Run Lead
DXC Technology
The Walbrook Building, 25 Walbrook, London, EC4N 8AQ, UK
t: +44 (0)20.3604.3154 | m: +44 (0)7826.943110 | ptiwari30@csc.com | www.dxc.com 

"""

try:
   smtpObj = smtplib.SMTP('smtp.xchanginghosting.com')
   smtpObj.sendmail(sender, receivers, message)
   print ( "Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")