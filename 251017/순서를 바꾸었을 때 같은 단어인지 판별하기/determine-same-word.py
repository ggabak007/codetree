word1 = input()
word2 = input()

# Please write your code here.
w1 = sorted(word1)
w2 = sorted(word2)
k = 0

if len(w1)!=len(w2):
    k+=1
if len(w1) == len(w2):
    for i in range(len(w1)):
        if(w1[i]!=w2[i]):
            k+=1
if k==0:
    print('Yes')
else:
    print('No')