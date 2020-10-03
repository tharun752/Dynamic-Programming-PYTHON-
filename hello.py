#code
md=1000000007
def power(x,y):
    if(y==0):
        return 1
    tmp=power(x,y//2)
    if(y%2):
        return (x*tmp*tmp)%md
    else:
        return (tmp*tmp)%md
    

def rev(n):
    re=0
    while(n>0):
        re=re*10+(n%10)
        n=n//10
    return re


for _ in range(int(input())):
    n=int(input())
    print(power(n,rev(n)))