#200=성공을 의미하는 숫자

from asyncore import write
from unittest import result
from urllib import response
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
url = "https://datalab.naver.com"
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

rank = 1

results = soup.findAll('span','item_titles')

print(response.text)

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%y년 %m월 %d일일의 실시간 검색어 순위입니다 \n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank +=1