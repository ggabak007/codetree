n = int(input())

# Please write your code here.

def four(n):
    k=1
    for i in range(n):
        while(1):
            print(k,end=' ')
            if k%n==0:
                print('\n')
                k+=1
                break
            k+=1

four(n)