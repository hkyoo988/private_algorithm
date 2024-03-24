import sys
from collections import deque

n, m, k, x = tuple(map(int, sys.stdin.readline().split()))
X = x
arr = [
    []
    for _ in range(n+1)
]

for _ in range(m):
    a, b = tuple(map(int, sys.stdin.readline().split()))

    arr[a].append(b)

distance = [0]*(n+1)
q = deque()
q.append(x)
while q:
    x = q.popleft()

    if distance[x] < k:
        for i in arr[x]:
            if distance[i] == 0:
                q.append(i)
                distance[i] = distance[x]+1
            

distance[X] = 0
found = False
for city, d in enumerate(distance[1:]):
    if d == k:
        print(city+1)
        found = True

# 최단 거리가 k인 도시가 없을 경우 -1을 출력합니다.
if not found:
    print(-1)