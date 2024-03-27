import sys
import heapq

V, e = tuple(map(int, sys.stdin.readline().split()))
visited = [sys.maxsize]*(V+1)

k = int(sys.stdin.readline().rstrip())

arr = [[] for _ in range(V+1)]
for _ in range(e):
    u, v, w = tuple(map(int, sys.stdin.readline().split()))

    arr[u].append((v, w))

pq = [(0, k)]
visited[k] = 0
while pq:
    w1, v = heapq.heappop(pq)

    for i in arr[v]:
        v2, w2 = i
        if visited[v2] > w1 + w2:
            visited[v2] = w1 + w2
            heapq.heappush(pq, (w1+w2, v2)) 

for i in range(1, V+1):
    if i == k:
        print(0)
    else:
        if visited[i] == sys.maxsize:
            print("INF")
        else:
            print(visited[i])
        