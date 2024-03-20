n ,k = tuple(map(int, input().split()))

arr = [
    int(input())
    for _ in range(n)
]

arr.sort()

start = 0
end = (sum(arr)+k)//len(arr)
ans = 0
while start <= end:

    team_level = (start + end) // 2
    up = k
    min_level = arr[0]

    for i in range(n):
        if arr[i] < team_level:
            up -= team_level - arr[i]
            if up < 0:
                min_level = arr[i]
                break
        else:
            min_level = team_level
        if i == n-1:
            min_level = team_level

    if team_level > min_level:
        end = team_level -1
    
    if team_level <= min_level:
        ans = team_level
        start = team_level + 1


print(ans)