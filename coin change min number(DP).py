def minimumNumberOfCoins(coins,numberOfCoins,value):
    a=[[-1]*(numberOfCoins+1) for _ in range(value+1)]
    for i in range(numberOfCoins):
        a[0][i]=0
    for i in range(1,value+1):
        a[i][0]=999
        
    coins.sort()
    for i in range(1,value+1):
        for j in range(1,numberOfCoins+1):
            temp1=a[i][j-1]
            temp2=999
            if(i>=coins[j-1]):
                temp2=a[i-coins[j-1]][j]
            a[i][j]=min(temp1,temp2+1)
    print(a[-1][-1])

                

    

minimumNumberOfCoins([1,2,3],3,5)