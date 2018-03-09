# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     猜数字
   Description :
   Author :       pan_qiang
   date：          2018-03-08
-------------------------------------------------
   Change Activity:
                   2018-03-08:
-------------------------------------------------
"""
__author__ = 'pan_qiang'
import random
print('--------猜一猜游戏------------')
num1 = int(input("请输入开始的区间数："))
num2 = int(input("请输入结束的区间数："))
number = random.randint(num1,num2)
s = 1
#while True:
while s <= 2:
        temp = int(input('猜一个数字：'))
        s += 1
        if number == temp:
                print('恭喜你猜对了！')
                print("你猜了%d次"%s)
                break
        elif number > temp:
                print('小了')
        elif number < temp:
                print('大了')
        elif temp.isdigit():
                continue
else:
        print('超过2次，游戏结束，正确的数字是:%d'%number)