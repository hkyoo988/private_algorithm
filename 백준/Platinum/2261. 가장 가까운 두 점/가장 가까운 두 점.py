import sys

n = int(input())

arr = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

arr.sort()

def get_dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2



def search(start, end):
    global distance
    if start == end:
        return sys.maxsize
    
    if end - start == 1:
        return get_dist(arr[start], arr[end]) 

    mid = (start + end) // 2

    distance = min(search(start, mid), search(mid, end))
    
    candidates = [] # 후보군 탐색
    for i in range(start, end+1):
        if (arr[mid][0] - arr[i][0])**2 < distance:
            candidates.append(arr[i])

    candidates.sort(key=lambda x: x[1])

    for i in range(len(candidates) - 1):
        for j in range(i+1, len(candidates)):
            if (candidates[i][1] - candidates[j][1])**2 < distance:
                distance = min(distance, get_dist(candidates[i], candidates[j]))
            else:
                break

    return distance
print(search(0, n-1))