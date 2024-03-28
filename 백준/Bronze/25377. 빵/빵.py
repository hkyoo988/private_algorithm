import sys

n = int(sys.stdin.readline().rstrip())

result = sys.maxsize
for _ in range(n):
    a, b = tuple(map(int, sys.stdin.readline().split()))

    if a <= b:
        result = min(result, b)

if result == sys.maxsize:
    print(-1)
else:
    print(result)