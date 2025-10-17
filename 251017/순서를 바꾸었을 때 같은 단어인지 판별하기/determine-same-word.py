word1 = input()
word2 = input()

# Please write your code here.
w1 = sorted(word1)
w2 = sorted(word2)

if len(w1)!=len(w2):
    print('No')
if len(w1) == len(w2):
    if w1 == w2:
        print('Yes')