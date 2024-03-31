import sys

equation = sys.stdin.readline().rstrip().split("-")

for i in range(len(equation)):
    equation[i] = list(map(int, equation[i].split("+")))

result = sum(equation[0])
for i in equation[1:]:
    result -= sum(i)

print(result)