import sys

n = int(input())

arr = [
    list(input())
    for _ in range(n)
]

def partition(n, x, y):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != arr[x][y]:
                print('(', end="")
                partition(n//2, x, y)
                partition(n//2, x, y + n//2)
                partition(n//2, x + n//2, y)
                partition(n//2, x + n//2, y + n//2)
                print(')', end="")
                return
        if i == x+n-1:
            print(arr[x][y], end="")        

partition(n, 0, 0)