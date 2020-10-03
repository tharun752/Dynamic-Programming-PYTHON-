def fun(n,l,arr):
    for i in range(1,n):
        mx=l[i]
        for j in range(0,i):
            if(arr[j]>arr[i]):
                mx=max(mx,1+l[j])
        l[i]=mx
    return l[n-1]
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    l=[1]*n
    
    r=fun(n,l,arr)
    print(max(l))