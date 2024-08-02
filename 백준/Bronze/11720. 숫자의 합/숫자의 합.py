import sys

n = int(sys.stdin.readline())
m = list(sys.stdin.readline().rstrip())
ans = 0

for i in m:
    ans += int(i)

print(ans)
