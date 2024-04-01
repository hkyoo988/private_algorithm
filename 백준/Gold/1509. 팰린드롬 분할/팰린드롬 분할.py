import sys

arr = list(sys.stdin.readline().rstrip())
n = len(arr)

dp = [
    [0]*(n)
    for _ in range(n)
]

for i in range(n-1):
    dp[i][i] = 1
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

dp[-1][-1] = 1

for step in range(2, n):
    for i in range(n-step):
        j = i + step
        if dp[i+1][j-1] == 1 and arr[i] == arr[j]:
            dp[i][j] = 1

result_dp = [
    [0]*(n+1)
    for _ in range(n+1)
]

for i in range(1, n+1):
    result_dp[i][i] = 1
    result_dp[0][i] = sys.maxsize
for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i-1][j-1] != 1:
            result_dp[i][j] = min(result_dp[i-1][j], result_dp[i][j-1]+1)
        else:
            result_dp[i][j] = min(result_dp[i-1][i-1]+1, result_dp[i-1][j])

print(result_dp[-1][-1])