import random


def insert_sort(li):
    if len(li) < 2:
        return li
    else:
        for i in range(1, len(li)):
            j = i - 1
            temp = li[i]
            while j >= 0 and temp < li[j]:
                li[j+1] = li[j]
                j -= 1
            li[j+1] = temp


array = [i for i in range(10)]
print(array)
random.shuffle(array)
insert_sort(array)
print(array)

