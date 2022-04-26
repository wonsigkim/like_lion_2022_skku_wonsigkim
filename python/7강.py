# -*- coding: utf-8 -*-

import random
from xxlimited import foo

food = ["된장찌개","피자","제육볶음","햄버거","마라탕"]
information = {"고향":"일산","좋아하는 것":"운동","좋아하는 음식":"햄버거"}
information["특기"] = "그림"
information["사는 곳"] = "서울"
del information["좋아하는 음식"]
print(information)
print(len(information))
information . clear()
print(information)
print(food[1])
food.append("김밥")
del food[0]
print(food)