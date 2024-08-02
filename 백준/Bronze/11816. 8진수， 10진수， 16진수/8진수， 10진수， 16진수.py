import sys

n = sys.stdin.readline().rstrip()

if n.startswith("0x"):
    ans = int(n, 16)
elif n.startswith("0"):
    ans = int("0o"+n[1:], 8)
else:
    ans = n

print(ans)