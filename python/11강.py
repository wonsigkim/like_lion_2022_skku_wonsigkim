# -*- coding: utf-8 -*-

import random

food = random.choice(["된장찌개", "피자", "제육볶음", "된장찌개"])

print(food)
if(food == "제육볶음"):
    print("곱빼기 주세요")

else:
    print("그냥 주세요")

print("종료")