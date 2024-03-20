n, m, l = tuple(map(int, input().split()))

shooter = list(map(int, input().split()))

animals = [
    tuple(map(int, input().split()))
    for _ in range(m)
]
cnt = 0
for x, y in animals:
    distance = l - y
    target = x
    start = 0
    end = n-1

    while start <= end:
        
        mid = (start+end) // 2

        if target - distance <= shooter[mid] <= target + distance:
            cnt += 1
            break
        
        if shooter[mid] <= target:
            start = mid + 1
        elif shooter[mid] > target:
            end = mid - 1

print(cnt)        
