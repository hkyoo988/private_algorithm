n = int(input())

ans = n
for i in range(n, 0, -1):
    temp = sum(list(map(int, list(str(i)))))
    if i + temp == n:
        ans = min(ans, i)

print(ans if ans != n else 0)
