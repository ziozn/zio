# coding=gbk
"""
���쳲��������е�ǰ20����
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: ���
Date: 2018-03-02
"""
x = 0
y = 1
for _ in range(20):
    x, y = y, x + y
    print(x, end=' ')

