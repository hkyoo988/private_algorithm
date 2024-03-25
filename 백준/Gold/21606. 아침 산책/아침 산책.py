import sys

n = int(sys.stdin.readline())

arr = [0] + list(map(int, list(sys.stdin.readline().rstrip())))

route = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = tuple(map(int, sys.stdin.readline().split()))

    route[s].append(e)
    route[e].append(s)


def dfs(start):
    global cnt
    for i in route[start]:
        if not visited[i] and arr[i]:
            visited[i] = 1
            cnt += 1
        elif not visited[i] and not arr[i]:
            visited[i] = 1
            dfs(i)
            visited[i] = 0


cnt = 0
for idx, p in enumerate(arr):
    if p == 1:
        visited = [0]*(n+1)
        visited[idx] = 1
        dfs(idx)

print(cnt)