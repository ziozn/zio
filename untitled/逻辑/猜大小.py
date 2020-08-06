"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from random import randint
print('猜数字游戏')
i = 0
y = randint(1, 100)
while True:
    i += 1
    sum = int(input('第%d次输入数字:' % i))
    if y == sum:
        print('恭喜你猜对了')
        break
    elif sum < y:
        print('小了')
    elif sum > y:
        print('大了')
    else:
        print('请输入合理的数字')
