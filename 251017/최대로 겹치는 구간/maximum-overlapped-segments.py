n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
nums = []
for k in range(n):
    for i in range(segments[k][0],segments[k][1],1):
        nums.append(i)
nums.sort()
maxk = 0
k = 1
for i in range(len(nums)-1):
    if nums[i+1] == nums[i]:
        k +=1
    else:
        maxk = k
        k = 1
if k> maxk:
    print(k)
else:
    print(maxk)
    
