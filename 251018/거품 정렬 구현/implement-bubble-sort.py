n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for j in range(n):
    for i in range(n-1-j):
        if arr[i]>arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp

print(*arr)            