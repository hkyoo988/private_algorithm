import sys
from collections import deque

n, m, start = tuple(map(int, sys.stdin.readline().split()))

route = [
    [0]*(n+1)
    for _ in range(n+1)
]

for _ in range(m):
    p, q = tuple(map(int, sys.stdin.readline().split()))

    
    route[p][q] = 1
    route[q][p] = 1

visited = [0]*(n+1)

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()

        for i in range(1, n+1):
            if route[v][i] and not visited[i]:
                visited[i] = 1
                print(i, end=" ")
                q.append(i)

def dfs(start):

    for i in range(1, n+1):
        if route[start][i] and not visited[i]:
            visited[i] = 1
            print(i, end=" ")
            dfs(i)
    return

print(start, end=" ")
visited[start] = 1
dfs(start)

visited = [0]*(n+1)
print()

print(start, end=" ")
visited[start] = 1
bfs(start)