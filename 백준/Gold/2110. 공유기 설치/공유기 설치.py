N, C = tuple(map(int, input().split()))

wifi = [
    int(input())
    for _ in range(N)
]

wifi.sort()

def binary_search(left, right):
    result = 0
    while left <= right:
        curr = wifi[0]
        distance = (left + right) // 2
        cnt = 1
        for i in range(1, N):
            if wifi[i] >= distance + curr:
                cnt += 1
                curr = wifi[i]
        
        if cnt >= C:
            left = distance+1
            result = distance
        else:
            right = distance-1
    return result

print(binary_search(1, wifi[-1]-wifi[0]))
    