import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

arr = [
    [0]*(n+1)
    for _ in range(n+1)
]
def find_heavy(bid):
    global cnt
    for i in range(1, n+1):
        if arr[bid][i] and not visited[i]:
            cnt += 1
            visited[i] = 1
            find_heavy(i)

def find_light(bid):
    global cnt
    for i in range(1, n+1):
        if arr[i][bid] and not visited[i]:
            cnt += 1
            visited[i] = 1
            find_light(i)

for _ in range(m):
    p, q = tuple(map(int, sys.stdin.readline().split()))
    # q구슬 보다 무거운 p구슬
    arr[q][p] = 1

res = 0
mid = (n+1)//2
for i in range(1, n+1):
    cnt = 0
    visited = [0]*(n+1)
    visited[i] = 1
    # 무거운 구슬 개수 찾기
    find_heavy(i)

    if cnt >= mid: res += 1

    cnt = 0
    visited = [0]*(n+1)
    visited[i] = 1
    # 가벼운 구슬 개수 찾기
    find_light(i)
    if cnt >= mid: res += 1



print(res) 