import sys

n = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(n):
    c, r = tuple(map(int, sys.stdin.readline().split()))

    arr.append(("L", c-r))
    arr.append(("R", c+r))

# 인덱스 1은 내림차순 0은 오름차순에서 reverse를 설정해서 다시 1은 오름차순 0은 내림차순으로 바뀜
arr.sort(key=lambda x: (-x[1], x[0]), reverse=True)

stack = []
area = 1

for i in arr:
    d, l = i

    if d == "L":
        stack.append((d, l))
    else:
        sum_r = 0
        while True:
            prev_d, prev_l = stack.pop()
            if prev_d == "L":
                r = l - prev_l
                if r == sum_r:
                    area += 2
                else:
                    area += 1
                stack.append(("C", r))
                break
            else:
                sum_r += prev_l

print(area)