import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))
idx = 1
stack = []
num = len(arr)
for i in range(num):
    while stack and stack[-1] == idx:
        x = stack.pop()
        idx += 1

    stack.append(arr[i])

if stack:
    while True:
        if stack[-1] == idx:
            stack.pop()
            idx += 1
        else:
            print("Sad")
            break
        if not stack:
            print("Nice")
            break
else:
    print("Nice")