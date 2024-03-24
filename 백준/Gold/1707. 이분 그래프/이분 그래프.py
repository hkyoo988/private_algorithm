import sys
sys.setrecursionlimit(10**9)

def dfs(x):
    global result
    if result == 'NO':
        return
    
    for i in g[x]:
        if color[x] == color[i]:
            result = 'NO'
            return
        
        if not color[i]:
            if color[x] == 'R':
                color[i] = 'B'
                dfs(i)
            elif color[x] == 'B':
                color[i] = 'R'
                dfs(i)
            else:
                continue

t = int(sys.stdin.readline())
for _ in range(t):
    v, e = tuple(map(int, sys.stdin.readline().split()))

    g = {}
    for i in range(1, v+1):
        g[i] = []

    for _ in range(e):
        p, q = tuple(map(int, sys.stdin.readline().split()))

        g[p].append(q)
        g[q].append(p)

    color = [0]*(v+1)
    visited = [0]*(v+1)
    result = 'YES'
    for i in range(1, v+1):
        if not color[i]:
            color[i]= 'R'
            dfs(i)
        if result == 'NO':
            break
    
    print(result)