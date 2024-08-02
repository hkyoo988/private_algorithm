import sys

n = int(sys.stdin.readline())

arr = [0]*(n+1)
ans = []
for i in range(2, n+1) :
    if arr[i]:
        continue
    while n % i == 0:
        ans.append(i)
        n //= i
    
    for j in range(i, n+1, i):
        arr[j] = 1

for i in ans:
    print(i)