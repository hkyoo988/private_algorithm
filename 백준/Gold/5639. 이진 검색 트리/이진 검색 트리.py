import sys
sys.setrecursionlimit(10**9)

stack = []
while True:
    try:
        stack.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    
    mid = end+1

    for i in range(start+1, end+1):
        if stack[i] > stack[start]:
            mid = i
            break
    
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(stack[start])

postorder(0, len(stack)-1)
