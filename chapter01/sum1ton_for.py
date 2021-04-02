# 1부터 n까지 정수의 합 계산(for 문)

print('1부터 n까지 정수의 합 계산')
n = int(input('n값을 입력: '))

sum = 0
for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지의 정수의 합 {sum} ')
