import heapq
import random

li = list(range(100))
random.shuffle(li)
print(li)
li = list(map(lambda x: -x, li))
heapq.heapify(li)
for i in range(len(li)):
    print(heapq.heappop(li)*-1,end=',')
