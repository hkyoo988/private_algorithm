import sys
import heapq

n, m = tuple(map(int, sys.stdin.readline().split()))

arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = tuple(map(int, sys.stdin.readline().split()))

    arr[a].append((c, b))
    arr[b].append((c, a))

visited = [0]*(n+1)
def prim():
    hq = []
    heapq.heappush(hq, (0, 1))
    total = []
    while hq:
        c, s = heapq.heappop(hq)

        if not visited[s]:
            visited[s] = True
            total.append(c)

        if len(total) == n:
            break

        for c, v in arr[s]:
            if not visited[v]:
                heapq.heappush(hq, (c, v))


    return sum(total) - max(total)

print(prim())