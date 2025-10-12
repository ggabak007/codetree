n = int(input())
A = list(map(int, input().split()))
result = float('inf')
# Please write your code here.
for i in range(n):
    current = 0
    for j in range(n):
        k = abs(i-j)
        current += k * A[j]
    result = min(result,current)
print(result)

        