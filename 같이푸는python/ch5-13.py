#smptlib

#smpt서버에 연결
from email import message
from email.mime import image
import smtplib
from email.message import EmailMessage
import imghdr
from tkinter import image_types
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업입니다.")
message["Subject"] = "이것은 제목입니다"
message["From"] = "charles9804@likelion.org"
message["To"] = "charles9804@naver.com"

image = open("lion.png","rb")
with open("lion.png","rb") as image:
    image_file = image.read()

image_types = imghdr.what('lion',image_file)
message.add_attachment(image_file,maintype = 'image', subtype = 'image_types' ,filename = 'lion.png' )

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("charles9804@likelion.org","mnis1=f(x)")

reg = "^[a-zA-Z0-9.+_=]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
print(re.match(reg,"charles9804likelion.org"))

#smtp.send_message(message)
#smtp.quit()

#정규 표현식//^[a-zA-Z0-9.+_=]+@[a-zA-z0-9]+\.[a-zA-Z]{2,3}$
#{2,3}=최소 2회 최대3회 반복된다.



#add_attachment = 다르것이 첨부되어있다
#일반적인 text만 들어가 있는 경우 plain text type
#사진등 다른 항목이 포함될 경우 Mixed type
#add_attachment의 재료 3가지
#1.image(첨부할 파일의 내용)
#2.Maintype(image,video...)
#3. subtype(확장자/ png,jpg...)