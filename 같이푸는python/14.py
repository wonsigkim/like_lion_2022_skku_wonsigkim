#200=성공을 의미하는 숫자

from asyncore import write
from unittest import result
from urllib import response
import requests
from bs4 import BeautifulSoup
from datetime import datetime


url="https://www.daum.net"
response = requests.get(url)

#file = open("daum.html","w")
#file.write(response.text)
#file.close()


soup = BeautifulSoup(response.text, 'html.parser')
rank = 1
results = soup.findAll("a","link_favorsch")

text_rank_result = open("rank_results.txt", "w")

print(datetime.today().strftime("%y년 %m월 %d일의 실시간 검색어 순위입니다 + \n "))

for result in results:
    text_rank_result.write(str(rank))+"위"+result.get_text()+"\n"
    print(rank,"위 :", result.get_text(),"\n")
    rank +=1




#print(response.text)
#print(soup.title)
#print(soup.title.string)
# \n = 줄바꿈