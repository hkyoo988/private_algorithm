n = int(input())

dp = [0]*(n+1)

dp[1] = "SK"

for i in range(2, n+1):
    if dp[i-1] == "SK" or dp[i-3] == "SK":
        dp[i] = "CY"
    else:
        dp[i] = "SK"

print(dp[n])