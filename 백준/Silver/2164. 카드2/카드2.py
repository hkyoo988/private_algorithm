from collections import deque

n = int(input())
q = deque()
for i in range(1, n+1):
    q.append(i)

toggle = 0
while len(q) > 1:
    
    if toggle == 0:
        q.popleft()
        toggle = 1
    else:
        x = q.popleft()
        q.append(x)
        toggle = 0
    
print(q[0])
  
