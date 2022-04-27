# -*- coding: utf-8 -*-

import random
import time

for x in range(30):
    print(random.choice(["된장찌개","피자","제육볶음","햄버거","마라탕"]))
    print("이 문장도 반복되나?")


while True:
    print(random.choice(["된장찌개","피자","제육볶음","햄버거","마라탕"]))
    print("이 문장도 반복되나?")
    break
    time.sleep(1)