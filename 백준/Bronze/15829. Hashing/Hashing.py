n = int(input())

arr = list(input().rstrip())

ans = 0

for i in range(n):
    ans += (ord(arr[i]) - ord("a") + 1)*(31**i)

print(ans % 1234567891)
