print('세 정수의 최댓값을 구함')
a = int(input('정수 a의 값을 입력: '))
b = int(input('정수 b의 값을 입력: '))
c = int(input('정수 c의 값을 입력: '))

maximum = a 
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print(f'최댓값 {maximum}')
