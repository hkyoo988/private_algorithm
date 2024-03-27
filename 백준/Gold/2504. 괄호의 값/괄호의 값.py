import sys

arr = list(sys.stdin.readline().rstrip())
stack = []
tmp, ans = 1, 0
for i in range(len(arr)):
    if arr[i] == "(":
        tmp *= 2
        stack.append("(")
    elif arr[i] == "[":
        tmp *= 3
        stack.append("[")
    else:
        if arr[i] == ")":
            if not stack or stack.pop() != "(":
                ans = 0
                break
            if arr[i-1] in [")", "]"]:
                tmp //= 2
                continue
            ans += tmp
            tmp //= 2
        else:
            if not stack or stack.pop() != "[":
                ans = 0
                break
            if arr[i-1] in [")", "]"]:
                tmp //= 3
                continue
            ans += tmp
            tmp //= 3

if stack:
    print(0)
else:
    print(ans)