n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def merge_sort(ary):
    N = len(ary)//2
    left = ary[N:]
    right = ary[:N]
    
    sort_left = merge_sort(left)
    sort_right = merge_sort(right)

    return sort_left,sort_right

def merge(left,right):
    merge_list = []
    l , r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merge_list.append(left[l])
            l+=1
        else:
            merge_list.append(right[r])
            r+=1
    
    merge_list += left
    merge_right += right

    return merge_list
    

arr2 = merge_sort(arr)
print(*arr2)