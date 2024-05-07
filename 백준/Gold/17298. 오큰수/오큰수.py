n = int(input())

arr = list(map(int, input().split()))

stack = []

res = [-1]*(n)

for i in range(n-1, -1, -1):
    while stack:
        if stack[-1] > arr[i]:
            res[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(arr[i])

print(*res)