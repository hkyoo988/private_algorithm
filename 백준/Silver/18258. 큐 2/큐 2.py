from collections import deque
import sys    
s = deque()

n = int(input())
for i in range(n):
    c = sys.stdin.readline().split()
    if len(c) == 2:
        s.append(int(c[1]))
    else:
        if c[0] == "pop":
            if len(s) == 0:
                print(-1)
            else:
                print(s.popleft())
        elif c[0] == "size":
            print(len(s))
        elif c[0] == "empty":
            if len(s) == 0:
                print(1)
            else:
                print(0)
        elif c[0] == "front":
            if len(s) == 0:
                print(-1)
            else:
                print(s[0])
        else:
            if len(s) == 0:
                print(-1)
            else:
                print(s[-1])
