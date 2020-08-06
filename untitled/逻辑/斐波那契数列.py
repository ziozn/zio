# coding=gbk
"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
x = 0
y = 1
for _ in range(20):
    x, y = y, x + y
    print(x, end=' ')

