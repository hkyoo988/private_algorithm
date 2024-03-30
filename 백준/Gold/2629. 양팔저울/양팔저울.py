import sys

n = int(sys.stdin.readline().rstrip())

weight = [0] + list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())

bids = list(map(int, sys.stdin.readline().split()))

dp = [
    [0]*(sum(weight)+1)
    for _ in range(n+1)
]

dp[0][sum(weight)] = 1

for i in range(1, n+1):
    for j in range(1, sum(weight)+1):
        if dp[i-1][j]:
            dp[i][j] = 1
            if j-weight[i] > 0:
                dp[i][j-weight[i]] = 1
            if j-weight[i]*2 > 0:
                dp[i][j-weight[i]*2] = 1

for i in bids:
    if i > sum(weight):
        print("N")
        continue
    if dp[-1][i]:
        print("Y", end=" ")
    else:
        print("N", end=" ")