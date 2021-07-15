# 이진 검색 트리 클래스 BinarySearchTree 사용

from enum import Enum
from bst import BinarySearchTree

Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n) 

tree = BinarySearchTree()

while True:
    menu = select_Menu()

    if menu == Menu.삽입:
        key = int(input('삽입할 키 입력: '))
        val = input('삽입할 값 입력: ')
        if not tree.add(key, val):
            print('삽입에 실패')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키 입력: '))
        tree.remove(key)

    elif menu == Menu.검색:
        key = int(input('검색할 키 입력: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}')
        else:
            print('해당하는 데이터 없음')

    elif menu == Menu.덤프:
        tree.dump()

    elif menu == Menu.키의범위:
        print(f'키의 최솟값 {tree.min_key()}')
        print(f'키의 최대값 {tree.max_key()}')

    else:
        break 

