import sys
import heapq


n = int(sys.stdin.readline().rstrip())

hq = []

for _ in range(n):
    a, b, c = tuple(map(int, sys.stdin.readline().split()))

    heapq.heappush(hq, (b, c))

on = []
result = 0
while hq:
    b, c = heapq.heappop(hq)

    if not on:
        heapq.heappush(on, c)
    else:
        while on: 
            c2 = heapq.heappop(on)
            if c2 <= b:
                continue
            else:
                heapq.heappush(on, c2)
                break
        heapq.heappush(on, c)
    result = max(result, len(on))

print(result)