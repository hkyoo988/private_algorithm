from collections import deque
import sys

k = int(input())

s = deque()

for _ in range(k):
    n = int(sys.stdin.readline())

    if n == 0:
        s.pop()
    else:
        s.append(n)

result = 0

while s:
    result += s.pop()

print(result)