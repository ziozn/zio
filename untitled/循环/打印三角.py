i = int(input('请输入行数:'))

for x in range(i):
    for _ in range(x+1):
        print('*', end='')
    print()

for x in range(i):
    for _ in range(i-x):
        print(' ', end='')
    for _ in range(x+1):
        print('*', end='')
    print()
