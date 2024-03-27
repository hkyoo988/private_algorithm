import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())

arr = [[] for _ in range(n+1)]

e = [0]*(n+1)
for _ in range(m):
    start, end, t = tuple(map(int, sys.stdin.readline().split()))

    arr[start].append((end, t))
    e[end] += 1

START, END = tuple(map(int, sys.stdin.readline().split()))

q = deque()
q.append((START))
time, street = [0]*(n+1), [[] for _ in range(n+1)]
while q:
    x = q.popleft()

    for i in arr[x]:
        end, t = i
        e[end] -= 1
        if time[end] < time[x] + t:
            time[end] = time[x] + t
            street[end] = [x]
        elif time[end] == time[x] + t:
            street[end].append(x)
        if e[end] == 0:
            q.append((end))

# q = deque([END])
route = set()

def find_max_route(end):

    for i in street[end]:
        if (end, i) not in route:
            route.add((end, i))
            find_max_route(i)

find_max_route(END)
# while q:
#     x = q.popleft()

#     for i in street[x]:
#         if (x, i) not in route:
#             route.add((x, i))
#             q.append(i)

print(time[end])
print(len(route))