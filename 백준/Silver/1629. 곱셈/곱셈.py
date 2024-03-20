a, B, c = tuple(map(int, input().split()))

def calc(b):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    k = calc(b//2)%c
    if b % 2 == 0:
        return k*k%c
    else:
        return k*k*a%c
    

ans = calc(B)

print(ans)