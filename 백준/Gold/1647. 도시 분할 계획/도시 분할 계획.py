import sys
import heapq

def find_parent(x):
    if parent[x] != x:
        x = find_parent(parent[x])
    
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = tuple(map(int, sys.stdin.readline().split()))

hq = []

for _ in range(m):
    a, b, c = tuple(map(int, sys.stdin.readline().split()))
    heapq.heappush(hq, (c, a, b))

parent = [i for i in range(n+1)]
ways = []
while hq:
    c, a, b = heapq.heappop(hq)

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ways.append(c)

print(sum(ways)-max(ways))