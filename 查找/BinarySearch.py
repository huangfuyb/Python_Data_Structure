
def binary_search(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


def binary_search_rec(array, left, right, target):
    if left > right:
        return False
    else:
        mid = (left + right)//2
        print(mid)
        if array[mid] > target:
            return binary_search_rec(array, left, mid-1, target)
        elif array[mid] < target:
            return binary_search_rec(array, mid + 1, right, target)
        else:
            return True


array = [i for i in range(1, 34)]
result = binary_search_rec(array, 0, len(array)-1, 37)
print(result)
result = binary_search(array, 37)
print(result)