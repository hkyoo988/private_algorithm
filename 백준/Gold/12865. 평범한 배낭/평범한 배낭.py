import sys

n, k = tuple(map(int, sys.stdin.readline().split()))

item = []

for _ in range(n):
    w, v = tuple(map(int, sys.stdin.readline().split()))

    item.append((w, v))

dp = [0]*(k+1)
dp[0] = 1

for w, v in item:
    for i in range(k, 0, -1):
        if i - w >= 0 and dp[i-w]:
            dp[i] = max(dp[i], dp[i-w]+v)

print(max(dp)-1)