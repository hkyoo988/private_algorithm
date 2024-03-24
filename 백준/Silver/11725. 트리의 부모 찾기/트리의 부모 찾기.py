import sys
from collections import deque

n = int(sys.stdin.readline())
tree = {}
for i in range(1, n+1):
    tree[i] = []

for _ in range(n-1):
    x, y = tuple(map(int, sys.stdin.readline().split()))

    tree[x].append(y)
    tree[y].append(x)
parent = [0]*(n+1)
parent[1] = 1
def bfs(x):
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        for i in tree[a]:
            if not parent[i]:
                parent[i] = a
                q.append(i)
bfs(1)
for i in parent[2:]:
    print(i)
                