import sys
from collections import deque

n = int(input())

arr = [[] for _ in range(n+1)]
entrance = [0]*(n+1)
time = [0]*(n+1)
for j in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    time[j+1] = temp[0]

    temp = temp[1:] 
    for i in temp:
        if i == -1:
            continue
        
        arr[i].append(j+1)
        entrance[j+1] += 1

q = deque()
result = [0]*(n+1)
for i in range(1, n+1):
    if entrance[i] == 0:
        q.append(i)
        result[i] = time[i]

while q:
    b = q.popleft()
    for i in arr[b]:
        entrance[i] -= 1
        result[i] = max(result[i], result[b] + time[i])
        if entrance[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i], end='\n')