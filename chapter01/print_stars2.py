# *를 n개 출력. w개마다 줄바꿈

print('* 출력 ')
n = int(input('몇 개를 출력?: '))
w = int(input('몇 개마다 줄바꿈?: '))

for _ in range(n //w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
