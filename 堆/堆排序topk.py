# 有n个数，设计算法得到前k大的数。
def sift(li, low, high):
    pass
    # 建立小根堆


def topk(li, k):
    heap = li[0:k]
    for i in range((len(heap)-2)//2, -1, -1):
        sift(li, i, len(heap)-1)
    for i in li[k:]:
        if i > heap[0]:
            heap[0] = i
            sift(heap, 0, len(heap)-1)
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap

