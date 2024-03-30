import sys
T = int(sys.stdin.readline().rstrip())


for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline().rstrip())
    
    dp = [0]*(target+1)
    dp[0] = 1
    for j in arr:
        for i in range(1, target+1):
            if i-j >= 0:
                dp[i] = dp[i] + dp[i-j]


    print(dp[target])
