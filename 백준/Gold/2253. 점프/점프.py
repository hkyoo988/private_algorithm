import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

small = [
    int(sys.stdin.readline().rstrip())
    for _ in range(m)
]

# 현재 속도보다 더 큰 속도로 왔을 때를 조사하기 때문에 모든 돌의 속도 길이를 최대로 설정한다.
dp = [[10001]*int((2*n)**(0.5)+2) for i in range(n+1)]
dp[1][0] = 0

for i in range(1, n+1):
    if i in small:
        continue
    for j in range(1, int((2*i)**(0.5))+1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1


print(min(dp[n]) if min(dp[n]) != 10001 else -1)