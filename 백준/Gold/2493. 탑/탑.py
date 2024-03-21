import sys

n = int(input())

arr = [0] + list(map(int, sys.stdin.readline().split()))

receive = [0]*(n+1)
stack = [n]

for i in range(n-1, 0, -1):
    while stack:
        if arr[i] > arr[stack[-1]]:
            receive[stack[-1]] = i
            stack.pop()
        else:
            stack.append(i)
            break
    stack.append(i)

for i in range(1, len(receive)):
    print(receive[i], end=" ")