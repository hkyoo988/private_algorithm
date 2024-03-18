import sys

n = int(sys.stdin.readline())

cities = [
    list(map(int, input().split()))
    for _ in range(n)
]



ans = sys.maxsize
def traveling(x, y):
    global cost, ans
    if cost >= ans:
        return

    if y == start:
        for visit in visited:
            if not visit:
                return
        ans = min(ans, cost)
        return
    
    for i in range(n):
        if cities[y][i] and not visited[i]:
            visited[i] = True
            cost += cities[y][i]
            traveling(y, i)
            visited[i] = False
            cost -= cities[y][i]


for i in range(n):
    for j in range(n):
        if cities[i][j]:
            start = i
            cost = cities[i][j]
            visited = [False]*n
            visited[j] = True
            traveling(i, j)

print(ans)