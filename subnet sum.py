#code
def fun(n,a,b,c):
    if(n==0):
        return 0
    if(n<0):
        return -1
    
    t= max(fun(n-a,a,b,c),fun(n-b,a,b,c),fun(n-c,a,b,c))
    
    if(t==-1):
        return -1
    
    return 1+t
for _ in range(int(input())):
    n=int(input())
    print(fun(n,3,5,10))