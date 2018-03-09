# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     输出时间下一秒
   Description :
   Author :       pan_qiang
   date：          2018-03-08
-------------------------------------------------
   Change Activity:
                   2018-03-08:
-------------------------------------------------
"""
__author__ = 'pan_qiang'

timestr = input()
timelist = timestr.split(":")
h = int(timelist[0])
s = int(timelist[1])
m = int(timelist[2])
m +=1

if m == 60:
    s += 1
    m=0
    if s==60:
        h+=1
        s=0
        if h==24:
            h=0
            

print("%.2d:%.2d:%.2d"%(h,s,m))