import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

left = 0
right = arr[-1]

while left <= right:

    center = (left+right)//2

    wood = 0

    for i in range(n):
        if arr[i] > center:
            wood += arr[i] - center

    
    if wood < m:
        right = center-1
    elif wood > m:
        left = center+1
    else:
        right = center
        break

print(right)
