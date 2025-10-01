n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
def ary(ary):
    for i in range(0,n-1):
        for j in range(n-1-i):
            if ary[j] > ary[j+1]:
                temp = ary[j]
                ary[j] = ary[j+1]
                ary[j+1] = temp

            
        
        return ary
A =ary(A)
B =ary(B)
if A==B:
    print("Yes")
else:
    print("No")