import sys        
T = int(input())			
k = int(input())			
            
# cv, cn = list(), list()			
arr = []        
for i in range(k):			
    a, b = map(int, sys.stdin.readline().split())			
    arr.append([a, b])		
 
dp = [0]*(T+1)
dp[0] = 1
for coin, cnt in arr:
    for i in range(T, 0, -1):
        for j in range(1, cnt+1):
            num = coin*j
            if i-num >= 0:
                dp[i] += dp[i-num]
print(dp[T])