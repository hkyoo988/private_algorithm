import sys

n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()

def calc_tree(start):
    result = 0

    for i in range(n):
        num = arr[i] - start
        if num > 0:
            result += num
    return result

ans, get_tree = 0, 0
def cut_tree(bottom, top):
    global ans, get_tree

    while bottom <= top:
        # if get_tree < m:
        #     mid = (bottom + mid-1) // 2
        mid = (bottom + top) // 2

        get_tree = calc_tree(mid)

        if get_tree > m:
            ans = mid
            bottom = mid + 1
        elif get_tree == m:
            ans = mid
            break
        else:
            top = mid - 1
        
        # if bottom == top:
        #     h = calc_tree(bottom)
        #     ans = bottom
        #     break

cut_tree(0, arr[-1])

print(ans)