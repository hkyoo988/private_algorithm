import sys

n, m = tuple(map(int, sys.stdin.readline().rstrip().split()))

set_a = list(map(int, sys.stdin.readline().rstrip().split()))

set_b = list(map(int, sys.stdin.readline().rstrip().split()))

dict = {}

for i in set_a:
    if i not in dict:
        dict[i] = 1

for j in set_b:
    if j not in dict:
        dict[j] = 1
    else:
        del dict[j]
        
print(len(dict.keys()))