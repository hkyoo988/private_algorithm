import sys
import heapq

n = int(input())

num_heap = []
sum_heap = []
for _ in range(n):

    a = int(input())
    heapq.heappush(num_heap, a)

while len(num_heap) > 1:
    num1 = heapq.heappop(num_heap)
    num2 = heapq.heappop(num_heap)

    num3 = num1 + num2

    heapq.heappush(num_heap, num3)
    sum_heap.append(num3)

print(sum(sum_heap))