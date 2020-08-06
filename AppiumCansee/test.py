#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-01 11:33
# @Author  : Aries
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import re
from sys import getrefcount


# socket编程
# import socket
# s = socket.socket()
# s.connect(('127.0.0.1', 62001))
# print(s.recv(1024))
# print(1111)
# s.close()

# lambda 表达式
# n = lambda x: x ** 2 + 10
# print(n(10))

# re.split分割字符串
# a = re.split("[ 3 or 6]", "1234567689")
# print(a)

# args和kwargs用法
# def test_kwargs(first, *args, **kwargs):
# 	print(first)
# 	for i in args:
# 		print("args %s" % i)
# 	for k, v in kwargs.items():
# 		print("kwargs", (k, v))
# test_kwargs(1, 2, 3, 4, a0=1, a1=2, a3=4)

# 引用计数
# a1 = 10000
# print(getrefcount(a1))

# 排序
listDemo = [1, 3, 7, 3, 5, 7, 1, 2, 9, 3, 5, 4, 2, 8]
a = sorted(listDemo, reverse=True)
# listDemo.sort()
print(listDemo)

# 冒泡排序
for i in range(len(listDemo) - 1):
	for j in range(len(listDemo) - 1 - i):
		if listDemo[j] > listDemo[j+1]:
			listDemo[j], listDemo[j+1] = listDemo[j+1], listDemo[j]

print(listDemo)
