# 도수 정렬 알고리즘 구현

from typing import MutableSequence
def fsort(a: MutableSequence, max:int) -> None:
    # 도수 정렬
    n = len(a)                     # 정렬할 배열 a
    f = [0] * (max+1)              # 누적 도수 분포표 배열 f
    b = [0] * n                    # 작업용 배열 b

    for i in range(n):
        f[a[i]] += 1
    for i in range(1, max+1):
        f[i] += f[i-1]
    for i in range(n-1, -1, -1):
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
    for i in range(n):
        a[i] = b[i]

def counting_sort(a:MutableSequence) -> None:
    # 도수 정렬
    fsort(a, max(a))

if __name__ == '__main__':
    print('도수 정렬 수행')
    num = int(input('원소 수 입력: '))
    x = [None] * num
    
    for i in range(num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= 0:
                break
    
    counting_sort(x)

    print('오름차순으로 정렬완료')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
