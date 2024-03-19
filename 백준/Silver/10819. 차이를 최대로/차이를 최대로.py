import sys

N = int(sys.stdin.readline())

arr = list(map(int, input().split()))

used = [False]*N
ans = []
res = 0


def calc():
    result = 0
    for i in range(1, N):
        num = abs(ans[i-1]-ans[i])
        result += num

    return result


def backtrack(n):
    global res
    if len(ans) == N:
        res = max(res, calc())
        return

    if n >= N:
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            ans.append(arr[i])
            
            backtrack(n+1)

            used[i] = False
            ans.pop()

backtrack(0)
print(res)