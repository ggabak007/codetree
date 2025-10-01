n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def maxy(ary):
    for i in range(0,2*n-1):
        for j in range(2*n-1-i):
            if ary[j]>ary[j+1]:
                temp = ary[j]
                ary[j] = ary[j+1]
                ary[j+1] = temp
    return ary

max_num = []
data = maxy(nums)

for i in range(n):
    k = data[i]+data[2*n-i-1]
    max_num.append(k)

print(max(max_num))
