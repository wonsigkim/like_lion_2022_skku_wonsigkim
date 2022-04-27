# -*- coding: utf-8 -*-

for x in range(30):
    print(x)

foods = ["된장찌개", "피자", "제육볶음"]
print(foods)
for x in range(3):
    print(foods[x])
for x in foods:
    print(x)

information = {"고향":"일산","좋아하는 것":"운동","좋아하는 음식":"햄버거"}
for x, y in information.items():
    print(x)
    print(y)