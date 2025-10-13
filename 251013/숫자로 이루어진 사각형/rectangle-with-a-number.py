n = int(input())

# Please write your code here.

def four(n):
    k=1
    for _ in range(n):
        for _ in range(n):
            if k==10:
                k = 1
            print(k,end=' ')
            k+=1
        print('')
four(n)