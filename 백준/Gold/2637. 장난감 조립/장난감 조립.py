import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

p = [[] for _ in range(n+1)]
e = [0]*(n+1)
for _ in range(m):
    x, y, k = tuple(map(int, sys.stdin.readline().split()))

    p[y].append((x, k))
    e[x] += 1

q = deque()
basic = []
cost = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    if e[i] == 0:
        q.append(i)
        basic.append(i)
        cost[i][i] = 1

while q:
    y = q.popleft()

    for i in p[y]:
        x, k = i    
        e[x] -= 1
        for j in basic:
            cost[x][j] = cost[x][j] + cost[y][j]*k 
        if e[x] == 0:
            q.append(x)

for idx, c in enumerate(cost[n][1:]):
    if idx in basic:
        print(idx, cost[n][idx])
