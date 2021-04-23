import random


def select_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i+1, len(li)):
            if li[min_index] > li[j]:
                min_index = j

        li[i], li[min_index] = li[min_index], li[i]


array = [i for i in range(10)]
random.shuffle(array)
print(array)
select_sort(array)
print(array)