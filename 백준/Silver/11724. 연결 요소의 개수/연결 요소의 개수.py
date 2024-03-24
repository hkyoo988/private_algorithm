import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().split()))

arr = [
    [0]*(n+1)
    for _ in range(n+1)
]

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))

    arr[x][y] = 1
    arr[y][x] = 1

visited = [0]*(n+1)

def bfs(start):
    result = False
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for i in range(1, n+1):
            if arr[x][i] and not visited[i]:
                result = True
                q.append(i)
                visited[x] = 1
                visited[i] = 1
    return result

cnt = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    if bfs(i):
        cnt += 1

for i in visited[1:]:
    if i == 0:
        cnt += 1

print(cnt if n != 1 else 1)