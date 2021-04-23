import random


def bubble_sort(li):
    for i in range(len(li)-1):
        exchage = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchage = True
        if not exchage:
            return


li = list(i for i in range(10))
random.shuffle(li)
print(li)
bubble_sort(li)
print(li)
