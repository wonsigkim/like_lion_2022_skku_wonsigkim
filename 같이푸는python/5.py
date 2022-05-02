#200=성공을 의미하는 숫자

from urllib import response
import requests


url="https://www.naver.com/"
response = requests.get(url)

print(response.text)

#print(response.url)- url주소 불러오기

#print(response.content)-html,css코드 불러오기

#print(response.encoding)-인코딩 언어 불러오기(utf-8/acsii...)

#print(response.headers)-header tag정보 불러오기(날씨,날짜...)

#print(response.json)-json(javascript object notation) 자바를 객체로 만들때 사용하는 표현식

#print(response.links)-링크ㅡ 불러오기??

#print(response.ok)status_code가 200일때 True/400보다 클때 flase

#print(response.status_code)404/200으로 출력