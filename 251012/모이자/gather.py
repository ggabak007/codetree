n = int(input())
A = list(map(int, input().split()))
result = 0
# Please write your code here.
for _ in range(n):
    minx = 0
    for j in range(0,n-1,1):
        k = A[j]-A[j+1]
        minx += abs(k)
    result = min(result,minx)
print(result)

        