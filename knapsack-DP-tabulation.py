for _ in range(int(input())):
    weights=list(map(int,input().split()))
    values=list(map(int,input().split()))
    weight=int(input())
    dp=[[-1]*(weight+1) for _ in range(len(weights)+1)]
    for i in range(len(weights)+1):
        dp[i][0]=0
    for i in range(weight+1):
        dp[0][i]=0
    for i in range(1,len(weights)+1):
        for j in range(1,weight+1):
            if(weights[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(values[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
    print(dp[len(weights)][-1])
