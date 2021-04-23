
import random


def sift(li, low, high):
    temp = li[low]
    i = low
    j = 2*i + 1
    while j <= high:
        if j+1 <= high and li[j+1] > li[j]:
            j = j+1
        if temp < li[j]:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            li[i] = temp
            break
    li[i] = temp


array = [i for i in range(10)]
random.shuffle(array)
for i in range((len(array)-2)//2, -1, -1):
    sift(array, i, len(array)-1)
for i in range(len(array)-1, -1, -1):
    array[0], array[i] = array[i], array[0]
    sift(array, 0, i-1)
print(array)
