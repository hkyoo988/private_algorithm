import sys

text = list(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == "L":
        if text:
            stack.append(text.pop())
    elif command[0] == "D":
        if stack:
            text.append(stack.pop())
    elif command[0] == "B":
        if text:
            text.pop()
    else:
        text.append(command[1])

ans = text + stack[::-1]
print("".join(ans))