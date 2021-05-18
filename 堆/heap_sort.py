import heapq
import random

# li = list(range(100))
# random.shuffle(li)
# print(li)
# li = list(map(lambda x: -x, li))
# heapq.heapify(li)
# print(li)
# for i in range(len(li)):
#     print(heapq.heappop(li)*-1,end=',')


# def get_least_numbers_big_data(alist, k):
#     max_heap = []
#     length = len(alist)
#     if not alist or k <= 0 or k > length:
#         return
#     k = k - 1
#     for ele in alist:
#         ele = -ele
#         if len(max_heap) <= k:
#             heapq.heappush(max_heap, ele)
#         else:
#             heapq.heappushpop(max_heap, ele)
#
#     return map(lambda x:-x, max_heap)

def get_least_numbers_big_data(tinput, k):
    # write code here
    if len(tinput) < k:
        return []
    import heapq
    result = []
    for i in range(k):
        heapq.heappush(result, tinput[i] * -1)
    print(result)
    for j in range(k, len(tinput)):
        if tinput[j] < result[0] * -1:
            heapq.heappop(result)
            heapq.heappush(result, -1 * tinput[j])
    ans = []
    for m in range(k - 1, -1, -1):
        ans.append(heapq.heappop(result)*-1)
    return ans[::-1]

    # print(result)

if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3]
    # min_k = get_least_numbers_big_data(l, 3)
    s = get_least_numbers_big_data(l, 3)
    print(s)
    # print(list(min_k))