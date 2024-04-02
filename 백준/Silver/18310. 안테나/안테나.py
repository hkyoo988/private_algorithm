import sys

def calc(x):
    ans = 0
    for i in range(n):
        ans += abs(arr[i]-arr[x])
    return ans


n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

if n%2 != 0:
    mid = n//2
    ans = mid
else:
    m1 = n//2
    m2 = n//2 - 1
    if calc(m1) > calc(m2):
        ans = m2
    elif calc(m1) < calc(m2):
        ans = m1
    else:
        ans = min(m1, m2)

print(arr[ans])