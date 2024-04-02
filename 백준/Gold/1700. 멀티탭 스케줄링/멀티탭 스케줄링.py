import sys

def find_max_idx(start):
    max_idx = -1
    num = 0
    for j in using:
        try:
            num_idx = arr[start:].index(j)
        except:
            num_idx = k
        if max_idx < num_idx:
            max_idx = num_idx
            num = j
    return num

n, k = tuple(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

using = set()
cnt = 0
for i in range(k):
    using.add(arr[i])

    if len(using) > n:
        num = find_max_idx(i)
        using.discard(num)
        cnt += 1

print(cnt)