n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def up(list):
    lens = len(nums)
    for i in range(0,lens-1):
        for j in range(lens-1-i):
            if list[j]>list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list

def down(list):
    lens = len(nums)
    for i in range(0,lens-1):
        for j in range(lens-1-i):
            if list[j]<list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list

data = up(nums)
print(*data)
data = down(nums)
print(*data)