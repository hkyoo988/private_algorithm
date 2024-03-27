import sys

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    
    n = arr[0]
    
    if n == 0:
        break

    stack = []
    result = 0
    for idx, height in enumerate(arr):
        if idx == 0:
            continue
        if not stack:
            stack.append((idx, height))
        else:
            while stack:
                prev_idx, prev_height = stack.pop()
                width = 1
                if prev_height <= height:
                    stack.append((prev_idx, prev_height))
                    stack.append((idx, height))
                    break
                else:
                    if stack: width = stack[-1][0] + 1  
                result = max(result, (idx - width)*prev_height)
            stack.append((idx, height))

    while stack:
        prev_idx, prev_height = stack.pop()
        if len(stack) == 0:
            width = n 
        else:
            width = (n - stack[-1][0])
        result = max(result, prev_height * width)

    print(result)