import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    if n == 2:
        print(2)
        continue
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for j in [1, 2, 3]:
        for k in range(2, n+1):
            if k-j >= 0:
                dp[k] += dp[k-j]

    print(dp[n] if n != 0 else 0)