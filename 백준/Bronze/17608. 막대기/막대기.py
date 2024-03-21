import sys

n = int(input())

arr = [
    int(sys.stdin.readline())
    for _ in range(n)
]

max_bar = -sys.maxsize
cnt = 0
for i in range(n-1, -1, -1):
    if arr[i] > max_bar:
        cnt += 1
        max_bar = arr[i]

print(cnt)