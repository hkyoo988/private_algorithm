month, day = tuple(map(int, input().split()))
x, y = 1, 1

arr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
cnt = 0
while True:

    if x == month and y == day:
        print(arr[cnt])
        break

    y += 1
    cnt += 1

    if cnt == 7:
        cnt = 0

    if x in [1, 3, 5, 7, 8, 10, 12]:
        if y > 31:
            x += 1
            y = 1
    elif x in [4, 6, 9, 11]:
        if y > 30:
            x += 1
            y = 1
    else:
        if y > 28:
            x += 1
            y = 1
