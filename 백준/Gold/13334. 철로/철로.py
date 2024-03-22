import sys
import heapq

n = int(input())
arr = []
for _ in range(n):
    p, q = tuple(map(int, sys.stdin.readline().split()))
    arr.append((p,q))

h = []
l = int(input())
for i in arr:
    p, q = i

    if l >= abs(p-q):
        if p < q:
            heapq.heappush(h, (q, p))
        else:
            heapq.heappush(h, (p, q))

ans = 0

cnt = 0

start = []
while h:
    q, p = heapq.heappop(h)

    if not start:
        heapq.heappush(start, p)
        cnt += 1
    else:
        heapq.heappush(start, p)
        while start:
            p2 = heapq.heappop(start)
            if q - l > p2:
                cnt -= 1
            else:
                heapq.heappush(start, p2)
                break
        cnt += 1
    ans = max(ans, cnt)

print(ans)
    