import sys

n = int(sys.stdin.readline().rstrip())
string = list(sys.stdin.readline().rstrip())
detection = False
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
curr = ""
ans = []
for i in string:
    if i not in num:
        if len(curr) < 7 and len(curr) != 0:
            ans.append(int(curr))
        curr = ""
        continue
    curr += i
if len(curr) < 7 and len(curr) != 0:
    ans.append(int(curr))
print(sum(ans))