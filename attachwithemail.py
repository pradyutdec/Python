import smtplib
import base64

filename = "C:/Users/tiwarip/Documents/Personal/Python/File/test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'ptiwari30@csc.com'
reciever = 'pradyutdxc@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From pradyut <Ptiwari30@csc.com>
To: To Pradyutdxc <pradyutdxc@gmail.com>
Subject: Python Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
   smtpObj = smtplib.SMTP('smtp.xchanginghosting.com')
   smtpObj.sendmail(sender, reciever, message)
   print ("Successfully sent email")
except Exception:
   print ("Error: unable to send email")