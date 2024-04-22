import sys

n = int(input())
cnt = 0

# if n <= 3:
#     cnt = 1
# else:
#     while True:
#         m = n % 3
#         if n % 3 == 0:
#             n //= 3
#             cnt += 1
#         else:
#             if n % 2**(m+1) == 0:
#                 n //= 2**m
#                 cnt += m
#             else:
#                 n -= m
#                 cnt += m
#         if n == 1:
#             break

# print(cnt)

dp = [sys.maxsize]*(n+1)
dp[n] = 0
for i in range(n, 1, -1):
    dp[i-1] = min(dp[i-1], dp[i]+1)
    if i % 3 == 0:
        dp[i//3] = min(dp[i//3], dp[i]+1)
    if i % 2 == 0:
        dp[i//2] = min(dp[i//2], dp[i]+1)
print(dp[1])