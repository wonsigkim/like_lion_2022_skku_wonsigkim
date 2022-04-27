# -*- coding: utf-8 -*-

food = ["된장찌개", "피자", "제육볶음", "된장찌개"]
food_set = set(food)

print(food_set)
print(food)

menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "김치찌개", "콩나물국밥"])
menu3 = menu1 - menu2

print(menu3)



#####합집합|   교집합&    차집합-