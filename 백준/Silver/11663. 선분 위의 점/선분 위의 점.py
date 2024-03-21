import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

spot = list(map(int, sys.stdin.readline().split()))

lines = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

spot.sort()

def find_idx(left, right, target):
    ans = 0
    while left <= right:

        center = (left + right) // 2

        if target < spot[center]:
            if center == 0:
                break
            right = center - 1
        elif target > spot[center]:
            ans = center
            left = center + 1
        else:
            ans = center
            break
        
    return ans


for line in lines:
    start, end = line

    start_spot = find_idx(0, n-1, start)
    end_spot = find_idx(0, n-1, end)

    if spot[start_spot] < start:
        start_spot += 1
    
    if spot[end_spot] > end:
        end_spot -= 1

    if start_spot > end_spot:
        print(0)
    else:
        print(end_spot-start_spot+1)

