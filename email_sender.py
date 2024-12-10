# email_sender.py  

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_newsletter(subject, body, recipients):
    sender_email = "[email]@gmail.com"
    sender_password = "[password]"

    # email server setup 
    server = smtplib.SMTP ("smtp.gmail.com", 587) # 587 is default SMTP port
    server.starttls()
    server.login(sender_email, sender_password)

    # email message setup
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # send email
    for recipient in recipients:
        msg["To"] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())
    
    server.quit()
