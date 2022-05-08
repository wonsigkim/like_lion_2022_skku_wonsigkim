#smptlib

#smpt서버에 연결
from email import message
import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업입니다.")
message["Subject"] = "이것은 제목입니다"
message["From"] = "charles9804@likelion.org"
message["To"] = "charles9804@naver.com"

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("charles9804@likelion.org","mnis1=f(x)")
print(smtp.send_message)
smtp.quit



#MIME = 전자우편을 위한 인터넷 표준 형식
#header 부분 = [] = ""로 작성
#content 부분 = .set_content()로 작성