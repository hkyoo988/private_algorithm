n = int(input())

flag_a = [False]*n
flag_b = [False]*(2*n+1)
flag_c = [False]*(2*n+1)

# i가 행
cnt = 0
def set(i):
    global cnt
    # j가 열
    for j in range(n):
        if (not flag_a[j]) and (not flag_b[i+j]) and (not flag_c[i-j+n-1]):
            if i == n-1:
                cnt += 1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1] = False

set(0)
print(cnt)