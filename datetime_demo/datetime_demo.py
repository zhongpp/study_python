#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import time

now = datetime.now()
print(type(now))

# 指定时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "2016-03-20 11:45:39"
print(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))

a = '2017/11/6 06:35:32'
a = time.mktime(time.strptime(a, "%Y/%m/%d %H:%M:%S"))
print(a)
after = int(a) + int(8 * 3600)
print(after)
# print(time.strftime("%Y/%m/%d %H:%M:%S"), after)

a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
