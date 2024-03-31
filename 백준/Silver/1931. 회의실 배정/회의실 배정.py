import sys

n = int(sys.stdin.readline())

arr = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

arr.sort(key=lambda end: (end[1], end[0]))

prev = 0
cnt = 0
for i in arr:
    x, y = i
    if prev <= x:
        cnt += 1
        prev = y

print(cnt)