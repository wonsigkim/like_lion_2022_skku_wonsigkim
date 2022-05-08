#200=성공을 의미하는 숫자

from urllib import response
import requests
from bs4 import BeautifulSoup


url="https://www.naver.com/"
response = requests.get(url)

#print(response.text)

print(BeautifulSoup(response.text, 'html.parser'))