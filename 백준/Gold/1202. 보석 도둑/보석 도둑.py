import sys
import heapq

n, k = tuple(map(int, sys.stdin.readline().split()))

dia = []
for _ in range(n):
    w, v = tuple(map(int, sys.stdin.readline().split()))

    dia.append((w, v))

dia.sort()

bags = []
for _ in range(k):
    w = int(sys.stdin.readline().rstrip())
    heapq.heappush(bags, w)

cnt = 0; tmp = []
while bags:
    # 가장 작은 가방 무게
    c = heapq.heappop(bags)

    while dia and dia[0][0] <= c:
        heapq.heappush(tmp, -dia[0][1])
        heapq.heappop(dia)
    
    if tmp:
        cnt -= heapq.heappop(tmp)
    
print(cnt)