import sys

n = int(sys.stdin.readline().rstrip())

arr = [0] + list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())

q = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

dp = [
    [0]*(n+1)
    for _ in range(n+1)
]

for i in range(n+1):
    dp[i][i] = 1
for i in range(n):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for step in range(2, n):
    for i in range(n-step+1):
        if i + step <= n and arr[i] == arr[i+step] and dp[i+1][i+step-1]:
            dp[i][i+step] = 1


for x, y in q:
    if dp[x][y]:
        print(1)
    else:
        print(0)