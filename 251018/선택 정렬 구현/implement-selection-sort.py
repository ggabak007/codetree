n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(len(arr)-1):
    minn = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[minn]:
            minn = j
    tem = arr[i]
    arr[i] = arr[minn]
    arr[minn] = tem

print(*arr)