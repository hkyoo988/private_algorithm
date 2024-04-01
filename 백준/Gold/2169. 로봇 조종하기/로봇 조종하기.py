import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

dp = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

for i in range(1, m):
    dp[0][i] += dp[0][i-1]

for i in range(1, n):
    left = dp[i][:]
    right = dp[i][:]
    for j in range(m):
        if j == 0:
            left[0] += dp[i-1][j] 
        else:
            left[j] += max(dp[i-1][j], left[j-1])

    for j in range(m-1, -1, -1):
        if j == m - 1:
            right[-1] += dp[i-1][j]
        else:
            right[j] += max(dp[i-1][j], right[j+1])
    for j in range(m):
        dp[i][j] = max(left[j], right[j])
print(dp[-1][-1])