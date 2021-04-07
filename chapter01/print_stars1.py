# *를 n개 출력, w개마다 줄바꿈

print('* 출력')
n = int(input('몇 개를 출력?: '))
w = int(input('몇 개마다 줄바꿈?: '))

for i in range(n):
    print('*', end='')
    if i % w == w-1:
        print()

if n % w:
    print()
