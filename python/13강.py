# -*- coding: utf-8 -*-

lunch = ["짜장면", "피자", "제육볶음", "짬뽕"]
while True:
    print(lunch)
    item = input("음식을 추가 해주세요: ")
    lunch.append(item)
    if(item== "q"):
        break
    else:
        lunch.append(item)

print(lunch)

set_lunch = set(lunch)