#code
def fun(arr,n,tar):
    if(tar==0):
        return 1
    if(n==0):
        return 0
    
    res=fun(arr,n-1,tar)
    if(arr[n-1]<=tar):
        res+=fun(arr,n,tar-arr[n-1])
    return res
for _ in range(int(input())):
    n=int(input())
    arr=[3,5,10]
    memo=[[-1,-1,-1,-1] for _ in range(n+1)]
    for i in range(4):
        memo[0][i]=1
    for j in range(1,n+1):
        memo[j][0]=0

    print(fun(arr,3,n))