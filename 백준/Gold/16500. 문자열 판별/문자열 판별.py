import sys

target = list(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

arr = [
    sys.stdin.readline().rstrip()
    for _ in range(n)
]

dp = [0]*(len(target)+1)
dp[0] = 1
for i in range(len(target)+1):
    for j in arr:
        if len(j) <= i and dp[i-len(j)] and target[i-len(j):i] == list(j):
            dp[i] = 1

print(dp[-1])