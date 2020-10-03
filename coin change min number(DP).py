def minimumNumberOfCoins(coins,numberOfCoins,value):
    a=[[-1]*(value+1) for _ in range(numberOfCoins)]
    for i in range(numberOfCoins):
        a[i][0]=0
    coins.sort()
    for i in range(numberOfCoins):
        for j in range(values+1):
            if(arr[i]>j):
                

    

minimumNumberOfCoins([1,2,3],3,5)