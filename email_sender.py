# email_sender.py  

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv

def send_newsletter(subject, body, recipients):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    # email server setup 
    server = smtplib.SMTP ("smtp.gmail.com", 587) # 587 is default SMTP port
    server.starttls()
    server.login(sender_email, sender_password)

    # email message setup
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # send email
    for recipient in recipients:
        msg["To"] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())
    
    server.quit()
