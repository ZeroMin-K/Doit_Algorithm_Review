# 힙 정렬 알고리즘 구현(heapq.push, heapq.pop 사용)

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    # 힙정렬 
    
    heap = []
    for i in a:
        heapq. heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap) 
    
if __name__ == '__main__':
    print('힙 정렬 수행')
    num = int(input('원소 수 입력: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    print('오름차순으로 정렬 완료')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
