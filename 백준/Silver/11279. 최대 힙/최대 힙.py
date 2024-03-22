import heapq
import sys

t = int(input())
heap = []
for _ in range(t):
    oper = int(sys.stdin.readline())

    if oper == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-oper, oper))