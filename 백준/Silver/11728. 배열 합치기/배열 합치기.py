import sys

n, m = tuple(map(int, sys.stdin.readline().rstrip().split()))

set_a = list(map(int, sys.stdin.readline().rstrip().split()))
set_a.sort()
set_b = list(map(int, sys.stdin.readline().rstrip().split()))
set_b.sort()

result = []
pointer_a = 0
pointer_b = 0

while True:
    if set_a[pointer_a] >= set_b[pointer_b]:
        result.append(set_b[pointer_b])
        pointer_b += 1
    else:
        result.append(set_a[pointer_a])
        pointer_a += 1

    if pointer_a >= n:
        result.extend(set_b[pointer_b:])
        break
    
    if pointer_b >= m:
        result.extend(set_a[pointer_a:])
        break

print(*result)