import sys

def dfs(start):
    global cnt

    for i in range(1, n+1):
        if arr[start][i] and not visited[i]:
            visited[i] = 1
            cnt += 1
            dfs(i)

    return

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [
    [0]*(n+1)
    for _ in range(n+1)
]

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))

    arr[x][y] = 1
    arr[y][x] = 1

visited = [0]*(n+1)
cnt = 0
visited[1] = 1

dfs(1)

print(cnt)