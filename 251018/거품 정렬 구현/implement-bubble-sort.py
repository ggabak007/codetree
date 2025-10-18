n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for _ in range(n):
    for i in range(1,n-1):
        if arr[i-1]>arr[i]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp

print(*arr)            