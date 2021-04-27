# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    # 뮤터블 시퀀스 a의 원소를 역순으로 정렬 
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬')
    nx = int(input('원소 수 입력: '))
    x = [None] * nx  # 원소수가 nx인 리스트 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값 입력: '))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬 완료')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
