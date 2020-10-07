for _ in range(int(input())):
    coins=list(map(int,input().split()))
    n=int(input())
    a=[-1]*(n+1)
    a[0]=0
    for i in range(1,n+1):
        
        for j in range(len(coins)):
            if(i>=coins[j]):
                temp=a[i-coins[j]]
                if(temp!=-1):
                    a[i]=max(a[i],temp+1)
    print(a[-1])
