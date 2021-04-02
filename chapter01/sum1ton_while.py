# 1부터 n까지의 정수합 구하기 1(while 문)

print('1부터 n까지 정수의 합 계산')
n = int(input('n값을 입력: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합 = {sum}')
