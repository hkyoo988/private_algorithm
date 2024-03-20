import sys

t = int(input())

prime = [True]*100001
prime[0] = prime[1] = False

for j in range(2, int(10000**0.5)+1):
    if prime[j]:
        for i in range(j*j, 100001, j):
            prime[i] = False

for i in range(t):
    num = int(sys.stdin.readline()) 
    for j in range(int(num/2), 0, -1):
        if prime[j] and prime[num-j]:
            print(j, num-j)
            break