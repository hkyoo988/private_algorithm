import sys
from collections import deque

n, m = tuple(map(int , sys.stdin.readline().split()))

arr = [
    list(map(int, list(sys.stdin.readline().rstrip())))
    for _ in range(n)
]

visited = [
    [0]*m
    for _ in range(n)
]

cost = [
    [0]*m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or not arr[x][y]:
        return False

    return True 

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    dxs, dys = [1, 0 ,-1, 0], [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if can_go(nx, ny):
                visited[nx][ny] = 1
                cost[nx][ny] = min(cost[nx][ny], cost[x][y]+1) if cost[nx][ny] != 0 else cost[x][y] + 1
                q.append((nx, ny))

bfs(0, 0)
print(cost[n-1][m-1]+1)