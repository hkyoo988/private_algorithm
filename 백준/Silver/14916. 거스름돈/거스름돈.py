import sys

n = int(sys.stdin.readline().rstrip())

dp = [0]*(n+1)
def dp_func(n):
    if n < 5:
        return
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, n+1):
        if dp[i-5]:
            dp[i] = dp[i-5] + 1
        elif dp[i-2]:
            dp[i] = dp[i-2] + 1

dp_func(n)
if n < 5:
    if n == 2:
        print(1)
    elif n == 4:
        print(2)
    else:
        print(-1)
else:
    if dp[n] == 0:
        print(-1)
    else:
        print(dp[n])