import smtplib
from email.mime.text import MIMEText

sender = 'thejuttan2000@gmail.com' 
receivers = ['thejusofficial11@gmail.com']
port = 1025
msg = MIMEText('This mail is to demonstrate Simple mail transfer protocol')
msg['Subject'] = 'Test Mail' 
msg['From'] = 'thejuttan2000@gmail.com' 
msg['To'] = 'thejusofficial11@gmail.com'
server = smtplib.SMTP('localhost', port) 
server.sendmail(sender, receivers, msg.as_string()) 
print("Successfully Sent Email")
server.quit()