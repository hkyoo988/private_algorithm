import sys
import heapq

def find_parent(x):
    if visited[x] != x:
        visited[x] = find_parent(visited[x])

    return visited[x]

def union_parent(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a < b:
        visited[b] = a
    else:
        visited[a] = b

v, e = tuple(map(int, sys.stdin.readline().split()))

line = []

visited = [0]*(v+1)
for i in range(1, v+1):
    visited[i] = i

for _ in range(e):
    v1, v2, l = tuple(map(int, sys.stdin.readline().split()))

    heapq.heappush(line, (l, v1, v2))

ans = 0
while line:

    l, v1, v2 = heapq.heappop(line)

    # 부모가 같으면 스킵
    if find_parent(v1) != find_parent(v2):
        union_parent(v1, v2)
        ans += l
        
print(ans)