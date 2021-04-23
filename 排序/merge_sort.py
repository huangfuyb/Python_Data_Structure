import random
# merge function merge two sorted list to one list


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1

    li[low:high+1] = li_tmp


# li = [0, 1, 4, 12, 5, 6, 7, 8]
# merge(li, 0, 3, 7)
# print(li)
def merge_sort(li, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


li = list(range(100))
random.shuffle(li)
print(li)
merge_sort(li, 0, len(li)-1)
print(li)