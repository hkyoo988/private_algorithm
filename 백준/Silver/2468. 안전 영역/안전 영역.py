import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline().rstrip())

arr = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]


max_height = 0
for i in range(n):
    max_height = max(max_height, max(arr[i]))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y, h, visited):
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] > h:
            visited[nx][ny] = 1
            dfs(nx, ny, h, visited)

res = 0
for k in range(max_height-1, 0, -1):
    visited = [
        [0]*n
        for _ in range(n)
    ]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j, k, visited)
                cnt += 1

    res = max(res, cnt)

print(res if res != 0 else 1)