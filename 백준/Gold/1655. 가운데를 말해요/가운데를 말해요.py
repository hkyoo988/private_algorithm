import heapq
import sys

max_heap = []
min_heap = []
l = int(sys.stdin.readline())

for _ in range(l):
    n = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -n)
    else:
        heapq.heappush(min_heap, n)

    if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0]*(-1) > min_heap[0]:
        max_val = heapq.heappop(max_heap)*(-1)
        min_val = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)


    print(max_heap[0]*(-1))
