import sys
from collections import deque

n, k = tuple(map(int, sys.stdin.readline().split()))

coins = set()

for _ in range(n):
    coins.add(int(sys.stdin.readline().rstrip()))

sum_cost = [sys.maxsize]*(k+1)
coins = list(coins)
def bfs():
    q = deque()
    q.append((0, 0))

    while q:
        coin_num, prefix = q.popleft()

        for i in coins:
            if prefix+i <= k and sum_cost[prefix+i] > coin_num+1:
                sum_cost[prefix+i] = coin_num+1
                q.append((coin_num+1, prefix+i))

bfs()
if sum_cost[k] == sys.maxsize:
    print(-1)
else:
    print(sum_cost[k])
