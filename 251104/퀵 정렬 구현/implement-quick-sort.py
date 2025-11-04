n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def quick(ary):
    N = len(ary)
    if N<=1:
        return ary
    pivot = ary[0]
    left = []
    right = []
    for i in range(1,N):
        if pivot < ary[i]:
            right.append(ary[i])
        else:
            left.append(ary[i])
    return quick(left) + [pivot] + quick(right)


print(*quick(arr))