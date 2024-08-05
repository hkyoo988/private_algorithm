n = int(input())

curr = []
def backtrack():
    if len(curr) == n:
        for j in curr:
            print(j, end=" ")
        print()
        return
    
    for i in range(1, n+1):
        if i not in curr:
            curr.append(i)
            backtrack()
            curr.pop()

backtrack()