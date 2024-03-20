N = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

blue, white = 0, 0

def partition(n, x, y):
    global blue, white

    color = arr[x][y]

    for i in range(x, n+x):
        for j in range(y, n+y):
            if arr[i][j] != color:
                partition(n//2, x, y)
                partition(n//2, x+n//2, y)
                partition(n//2, x, y+n//2)
                partition(n//2, x+n//2, y+n//2)
                return
        
    if color == 1:
        blue += 1
    else:
        white += 1


partition(N, 0, 0)
print(white)
print(blue)