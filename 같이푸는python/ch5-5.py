#smptlib

#smpt서버에 연결
import smtplib
from socket import gaierror

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)

print(smtp)