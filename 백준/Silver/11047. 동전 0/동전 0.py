import sys

n, k = tuple(map(int, input().split()))

arr = []

for _ in range(n):
    a = int(sys.stdin.readline().rstrip())

    arr.append(a)

cnt = 0
for i in range(n-1, -1, -1):
    if arr[i] > k:
        continue
    
    cnt += k//arr[i]
    
    k %= arr[i]

    if k == 0:
        print(cnt)
        break