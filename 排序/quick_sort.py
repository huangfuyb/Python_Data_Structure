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


def quick_sort_no_rec(array):
    stack = []
    left = 0
    right = len(array)-1
    stack.append(left)
    stack.append(right)
    while stack:
        j = stack.pop()  # right
        i = stack.pop()  # left
        mid = partition(array, i, j)
        if mid - 1 > i:
            stack.append(i)  # left
            stack.append(mid-1)  # right
        if mid + 1 < j:
            stack.append(mid+1)  # left
            stack.append(j)  # right


random.seed(66)
arr_li = [i for i in range(10)]
random.shuffle(arr_li)
print(arr_li)
# quick_sort(arr_li, 0, len(arr_li)-1)
quick_sort_no_rec(arr_li)
print(arr_li)