for _ in range(int(input())):
    coins=list(map(int,input().split()))
    n=int(input())
    a=[999]*(n+1)
    a[0]=0
    for i in range(1,n+1):
        
        for j in range(len(coins)):
            if(i>=coins[j]):
                temp=a[i-coins[j]]
                if(temp!=999):
                    a[i]=min(a[i],temp+1)
    print(a)
