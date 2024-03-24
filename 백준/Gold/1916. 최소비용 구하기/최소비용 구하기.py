import sys
from collections import deque
import heapq

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

arr = [[] for _ in range(n+1)]

for _ in range(m):  
    s, e, c = tuple(map(int, sys.stdin.readline().split()))

    arr[s].append((e, c))


s, e = tuple(map(int, sys.stdin.readline().split()))

pq = []

heapq.heappush(pq, (0, s))
cost = [sys.maxsize]*(n+1)
cost[s] = 0
while pq:
    c, s = heapq.heappop(pq)

    if c == cost[s]:
        for ns, nc in arr[s]:
            c1 = c + nc
            if c1 < cost[ns]:
                cost[ns] = c1
                heapq.heappush(pq, (c1, ns))

print(cost[e])