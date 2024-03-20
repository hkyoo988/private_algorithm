import sys

n = int(input())

liquid = list(map(int, input().split()))
liquid.sort()

acid = []

alkali = []

for i in range(n):
    if liquid[i] > 0:
        acid.append(liquid[i]) 
    else:
        alkali.append(liquid[i])

start, end = 0, len(alkali)-1

measure = 0
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

if len(acid) >= 2:
    num = (acid[0] + acid[1]) - 2*measure 
    if abs(result) > abs(num):
        alkali_val = acid[0] - measure
        acid_val = acid[1] - measure
        result = num

if len(alkali) >= 2:
    num = (alkali[-1] + alkali[-2]) - 2*measure
    if abs(result) > abs(num):
        alkali_val = alkali[-2] - measure
        acid_val = alkali[-1] - measure
        result = num

print(alkali_val, acid_val)