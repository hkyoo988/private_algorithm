n = int(input())

arr = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

arr.sort()


def binary_search(left, right, value):
    global ans
    if left < right:
        center = (left + right) // 2

        if arr[center] == value:
            ans = True
            return
        elif arr[center] > value:
            binary_search(left, center-1, value)
        else:
            binary_search(center+1, right, value)

    if left == right and arr[left] == value:
        ans = True
        return 


for i in range(m):
    ans = False
    binary_search(0, n-1, arr2[i])
    if ans:
        print(1)
    else:
        print(0)