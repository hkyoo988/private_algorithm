import sys

n = int(input())

liquid = list(map(int, input().split()))
liquid.sort()

acid = []

alkali = []

for i in range(n):
    if liquid[i] > 0:
        acid.append(liquid[i]+1000000000) 
    else:
        alkali.append(liquid[i]+1000000000)

start, end = 0, len(alkali)-1

measure = 1000000000
result = sys.maxsize
for i in range(len(acid)):
    target = acid[i]
    start, end = 0, len(alkali)-1
    while start <= end:

        center = (start + end) // 2
        number = target + alkali[center]

        if measure*2 > number:
            start = center + 1
        elif measure*2 < number:
            end = center - 1
        else:
            result = 0
            acid_val = acid[i] - measure
            alkali_val = alkali[center] - measure
            break
        if abs(result) > abs(2*measure - number):
            result = number - 2*measure
            acid_val = target - measure
            alkali_val = alkali[center] - measure

for i in range(len(acid)-1):
    num = (acid[i] + acid[i+1]) - 2*measure 
    if abs(result) > abs(num):
        alkali_val = acid[i] - measure
        acid_val = acid[i+1] - measure
        result = num

for i in range(len(alkali)-1):
    num = (alkali[i] + alkali[i+1]) - 2*measure
    if abs(result) > abs(num):
        alkali_val = alkali[i] - measure
        acid_val = alkali[i+1] - measure
        result = num

print(alkali_val, acid_val)