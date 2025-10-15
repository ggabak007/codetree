n = int(input())

# Please write your code here.

def nums(num):
    result =0
    for i in range(num+1):
        result+=i
    return result//10

k = nums(n)

print(k)