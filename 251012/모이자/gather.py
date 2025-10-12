n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    minx = 0
    for j in range(n-1):
        k = A[j]+A[j+1]
        minx += abs(k)
    result = min(result,minx)
print(result)

        