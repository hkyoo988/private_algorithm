import sys
from collections import deque

r, c = tuple(map(int, sys.stdin.readline().split()))
arr = [
    list(sys.stdin.readline().rstrip())
    for _ in range(r)
]

def in_range(x, y):
    return 0 <= x and x < r and 0 <= y and y < c


q = deque()
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'D':
            end = (i,j)
        elif arr[i][j] == "S":
            start = ("S", i, j)
        elif arr[i][j] == "*":
            q.append(("*", i, j))

q.appendleft(start)


cnt = len(q)
day = 0
arrive = False
while q:
    a, x, y = q.popleft()
    cnt -= 1
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    
    if x == end[0] and y == end[1]:
        arrive = True
        break

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not arr[nx][ny] == "X" and arr[x][y] == a:
            if a == "S" and not arr[nx][ny] == "*" and not arr[nx][ny] == "S":
                arr[nx][ny] = "S"
                q.append(("S", nx, ny))
            elif a == "*" and not arr[nx][ny] == "D" and not arr[nx][ny] == "*":
                arr[nx][ny] = "*"
                q.append(("*", nx, ny))
    if cnt == 0:
        day += 1
        cnt = len(q)

                    
if arrive:
    print(day)
else:
    print("KAKTUS")
