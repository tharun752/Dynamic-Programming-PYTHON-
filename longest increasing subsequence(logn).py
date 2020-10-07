def binarys(tail,l,r,x):
    while(r>l):
        m=l+(r-l)//2
        if(tail[m]>=x):
            r=m
        else:
            l=m+1
    return r
def longest(arr,n):
    lis=[arr[0]]
    
    for i in range(1,n):
        if(arr[i]>lis[-1]):
            lis.append(arr[i])
        else:
            c=binarys(lis,0,len(lis)-1,arr[i])
            lis[c]=arr[i]
    print(len(lis))
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    longest(l,n)