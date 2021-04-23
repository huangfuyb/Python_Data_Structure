import random


def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        print(mid)
        # print(array)
        quick_sort(array, left, mid-1)
        quick_sort(array, mid+1, right)


random.seed(66)
arr_li = [i for i in range(10)]
random.shuffle(arr_li)
print(arr_li)
quick_sort(arr_li, 0, len(arr_li)-1)
print(arr_li)