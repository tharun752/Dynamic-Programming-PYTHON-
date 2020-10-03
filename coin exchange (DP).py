
for _ in range(int(input())):
    n=int(input())
    arr=[3,6,3]
    ex=[[-1]*4 for _ in range(n+1)]
    for i in range(4):
        ex[0][i]=1
    for j in range(1,n+1):
        ex[j][0]=0
    
    for i in range(1,n+1):#i=sum j=coins
        tmp1=tmp2=999
        for j in range(1,4):
            tmp1=ex[i][j-1]
            if(arr[j-1]<=i):
                ex[i][j]+=ex[i-arr[j-1]][j]
            
    print(ex)
    