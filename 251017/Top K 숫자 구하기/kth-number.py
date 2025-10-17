n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
i=1
for k in nums:
    if i==k:
        print(k)
        break
    i+=1