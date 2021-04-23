import random


def insert_sort(li):

    for i in range(1, len(li)):  # 摸到的牌
        j = i - 1   # 手里的牌
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        j = i-gap
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp


def shell_sort(li):
    gap = len(li)//2
    while gap >= 1:
        insert_sort_gap(li, gap)
        gap = gap//2


li = list(i for i in range(100))
random.shuffle(li)
print(li)
# insert_sort(li)
shell_sort(li)
print(li)

