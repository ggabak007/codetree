n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for i in range(n):
    if i==k-1:
        print(nums[i])
        break