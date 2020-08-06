"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

from random import randint
j = 1000
p = True
print('Craps赌博游戏')
while j > 0:
    wager = int(input('请下注:'))
    if wager > j:
        print('余额不足')
        print('你目前的余额为:%d   ' % j)
        wager = int(input('请重新下注:'))
    i = randint(2, 12)
    print('i点数：%d' % i)
    if i == 7 or i == 11:
        print('玩家胜')
        j += wager
    elif i == 2 or i == 3 or i == 12:
        print('庄家胜')
        j -= wager
    else:
        while p:
            print('游戏继续')
            k = randint(2, 12)
            print('k点数:%d' % k)
            if k == i:
                print('玩家胜')
                j += wager
                break
            elif k == 7:
                print('庄家胜')
                j -= wager
                break
            else:
                print('再摇一次')
    print('你的余额为:%d' % j)

print('你没钱了')
