n, k, t = input().split()
n, k = int(n), int(k)
word = [input() for _ in range(n)]

# Please write your code here.
str_list = []
word.sort()
for i in range(n):
    if(word[i].startswith(t)):
        str_list.append(word[i])

print(str_list[k-1])