from collections import deque

def dfs(idx, cnt):
    if cnt == 6:
        for i in range(n):
            if visited[i]:
                print(arr[i], end=" ")
        print()
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1,cnt + 1)
            visited[i] = 0

while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    
    if n == 0:
        break
    

    visited = [0]*n
    dfs(0, 0)

    print()