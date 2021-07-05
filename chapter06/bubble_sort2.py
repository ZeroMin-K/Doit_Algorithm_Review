# 버블 정렬 알고리즘 구현 (알고리즘 개선)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    # 버블 정렬
    n = len(a)
    for i in range(n-1):
        exchng = 0      # 패스에서 교환 횟수
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchng += 1
        if exchng == 0:
            break

if __name__ == '__main__':
    print('버블 정렬 수행')
    num = int(input('원소수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
