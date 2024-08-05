s = input()

arr = [-1]*26

for i in range(len(s)):
    idx = ord(s[i]) - ord("a")
    if arr[idx] == -1:
        arr[idx] = i

for j in arr:
    print(j, end=" ")