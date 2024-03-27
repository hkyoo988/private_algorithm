import sys
import heapq

n = int(sys.stdin.readline().rstrip())

max_h = []
min_h = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if i%2 == 0:
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if i>0 and min_h[0] < -max_h[0]:
        min_val = heapq.heappop(min_h)
        max_val = -heapq.heappop(max_h)

        heapq.heappush(min_h, max_val)
        heapq.heappush(max_h, -min_val)
    
    print(-max_h[0])