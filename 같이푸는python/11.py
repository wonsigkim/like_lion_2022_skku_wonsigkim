#200=성공을 의미하는 숫자

from urllib import response
import requests
from bs4 import BeautifulSoup


url="https://www.naver.com/"
response = requests.get(url)

print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print(soup.title.string)
print(soup.findAll('span'))



#beautifulsoup=function
#function 사용을 위해 데이터,파싱(parsing)방법이 필요함
#데이터= html/xml
#파싱=데이터를 분석하여 의미있게 변환하는 과정
#파서=parsing 할 수 있게 도와주는 도구
#[n:N] = n에서 N번째 까지의 값
#findAll('태그') '태그''에 해당되는 모든것 출력