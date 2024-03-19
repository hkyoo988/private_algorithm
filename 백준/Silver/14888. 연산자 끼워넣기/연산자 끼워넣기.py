import sys

N = int(input())

num = list(map(int, input().split()))

tmp = list(map(int, input().split()))

operation = {'0': tmp[0], '1': tmp[1], '2':tmp[2], '3':tmp[3]}

min_val, max_val = sys.maxsize, -sys.maxsize

def calc(oper, num, num2):
    if oper == 0:
        return num + num2
    elif oper == 1:
        return num - num2
    elif oper == 2:
        return num * num2
    else:
        if num < 0:
            return -(abs(num)//num2)
        else:
            return num // num2
    

def backtrack(idx):
    global result, min_val, max_val
    
    if idx == N:
        min_val = min(min_val, result)
        max_val = max(max_val, result)
        return

    

    for i in range(4):
        if operation[str(i)]:
            operation[str(i)] -= 1
            temp = result
            result = calc(i, result, num[idx])
            backtrack(idx+1)
            operation[str(i)] += 1
            result = temp

result = num[0]
backtrack(1)
print(max_val)
print(min_val)