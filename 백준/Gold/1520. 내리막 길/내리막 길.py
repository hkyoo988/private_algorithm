import sys
sys.setrecursionlimit(10**5)
m, n = tuple(map(int, sys.stdin.readline().split()))

arr = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

dp = [
    [-1]*n
    for _ in range(m)
]

def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]    

    ways = 0
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and arr[nx][ny] < arr[x][y]:
            ways += dfs(nx, ny)

    dp[x][y] = ways
    return ways

dfs(0, 0)
print(dp[0][0])