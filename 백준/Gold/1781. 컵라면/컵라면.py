import sys
import heapq

n = int(input())

hq = []
arr = []
for _ in range(n):
    end, num = tuple(map(int, sys.stdin.readline().split()))

    arr.append((end, num))
arr.sort(key=lambda x: x[0])
time = 1
for i in arr:
    end, num = i
    if end <= len(hq):
        while True:
            prev = heapq.heappop(hq)
            if prev > num:
                heapq.heappush(hq, prev)
                break
            if len(hq) < end:
                heapq.heappush(hq, num)
                break
    else:
        heapq.heappush(hq, num)

print(sum(hq))