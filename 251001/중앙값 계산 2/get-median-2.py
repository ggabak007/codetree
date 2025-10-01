n = int(input())
arr = list(map(int, input().split()))
num =[]
# Please write your code here.
def mdl_num(ary):
  lens = len(ary)
  for i in range(0,lens-1):
    for j in range(lens-1-i):
        if ary[j]>ary[j+1]:
            temp = ary[j]
            ary[j] = ary[j+1]
            ary[j+1] = temp
  return ary


for i in range(n):
  if (i+1)%2==1:
    sli = arr[:i+1]
    lis = mdl_num(sli)
    num.append(lis[i//2])

print(*num)