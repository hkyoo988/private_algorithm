import sys
n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))
start, end = 0, 0
partial_sum = arr[0]
ans = sys.maxsize
while True:
    if partial_sum < m:
        end += 1
        if end == n: break
        partial_sum += arr[end]
    else:
        partial_sum -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1



print(ans if ans != sys.maxsize else 0)