# 입력받은 정수의 부호(양수, 음수, 0) 출력

n = int(input('정수를 입력: '))

if n > 0:
    print('Positive')
elif n < 0:
    print('Negative')
else:
    print('0')
