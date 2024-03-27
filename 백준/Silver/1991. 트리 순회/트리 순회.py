import sys

n = int(sys.stdin.readline().rstrip())

dict = {}

for _ in range(n):
    root, left, right = tuple(sys.stdin.readline().split())

    dict[root] = (left, right)


def preorder(a):
    if a == ".":
        return
    print(a, end="")
    preorder(dict[a][0])
    preorder(dict[a][1])

def inorder(a):
    if a == ".":
        return
    inorder(dict[a][0])
    print(a, end="")
    inorder(dict[a][1])

def postorder(a):
    if a == ".":
        return
    postorder(dict[a][0])
    postorder(dict[a][1])
    print(a, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")