import sys
from collections import deque
m, n, h = tuple(map(int, sys.stdin.readline().split()))

def in_range(x, y, z):
    return 0 <= x < h and 0 <= y < n and 0 <= z < m

arr = []

for _ in range(h):
    temp = []
    temp = [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(n)
    ]
    arr.append(temp)

q = deque()
cnt, tomato = 0, 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i,j,k))
                cnt += 1
            if arr[i][j][k] == 0:
                tomato += 1

day = 0
changed = False
while q:
    x, y, z = q.popleft()
    cnt -= 1
    dxs, dys, dzs = [1,-1,0,0,0,0], [0,0,1,0,-1,0], [0,0,0,1,0,-1]
    for dx, dy, dz in zip(dxs, dys, dzs):
        nx, ny, nz = dx+x, dy+y, dz+z
        if in_range(nx, ny, nz) and not arr[nx][ny][nz]:
            arr[nx][ny][nz] = 1
            q.append((nx,ny,nz))
            tomato -= 1
            changed = True
    if cnt == 0 and changed:
        day += 1
        cnt = len(q)
        changed = False

print(day if tomato <= 0 else -1)