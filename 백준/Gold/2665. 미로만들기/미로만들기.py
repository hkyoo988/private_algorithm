import sys
from collections import deque


n = int(sys.stdin.readline())

arr = [
    list(map(int, list(sys.stdin.readline().rstrip())))
    for _ in range(n)
]

visited = [
    [sys.maxsize]*n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


q = deque()
q.append((0,0,0))
visited[0][0] = 0
while q:

    x, y, c = q.popleft()

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if in_range(nx, ny):
            if arr[nx][ny] and visited[nx][ny] > c:
                visited[nx][ny] = c
                q.append((nx, ny, c))
            elif not arr[nx][ny] and visited[nx][ny] > c+1:
                visited[nx][ny] = c+1
                q.append((nx, ny, c+1))

print(visited[n-1][n-1])