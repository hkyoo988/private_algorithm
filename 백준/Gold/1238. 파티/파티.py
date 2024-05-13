import heapq
import sys
input = sys.stdin.readline

"""
1238 파티

N->X로 가야함
도로는 총 M개
"""

N, M , X = map(int,input().split())
graph1 = [[] for i in range(N+1)]   #가는 길
dis1 = [float('inf')] * (N+1)
dis1[X] = 0

graph2 = [[] for i in range(N+1)] #돌아가는 길
dis2 = [float('inf')] * (N+1) 
dis2[X] = 0

for i in range(M):
    start, end, weight = map(int,input().split())
    graph1[end].append((weight, start))
    graph2[start].append((weight, end))

heap = [(0, X)]
while heap:
    w1, s = heapq.heappop(heap)

    if dis1[s] < w1:
        continue

    for w2, e in graph1[s]:
        if w1+w2 < dis1[e]:
            dis1[e] = w1+w2
            heapq.heappush(heap, (w1+w2, e))

heap = [(0, X)]
while heap:
    w1, s = heapq.heappop(heap)

    if dis2[s] < w1:
        continue

    for w2, e in graph2[s]:
        if w1+w2 < dis2[e]:
            dis2[e] = w1+w2
            heapq.heappush(heap, (w1+w2, e))

print(max(dis1[i] + dis2[i] for i in range(1, N+1)))

