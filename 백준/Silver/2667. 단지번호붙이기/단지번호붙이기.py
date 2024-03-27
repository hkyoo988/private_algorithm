import sys

n = int(sys.stdin.readline().rstrip())

arr = [
    list(map(int, list(sys.stdin.readline().rstrip())))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y):
    global cnt
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

visited = [
    [0]*n
    for _ in range(n)
]

result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j]:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)