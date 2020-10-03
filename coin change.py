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
    print(fun(arr,3,n))