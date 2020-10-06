def display(arr,m,n,re,str1,ans):

    if(re[m][n]==1):
        ans.append(str1[m-1])
        return display(arr,m-1,n-1,re,str1,ans)
    elif(re[m][n]==0):
        return display(arr,m,n-1,re,str1,ans)
    elif(re[m][n]==2):
        return display(arr,m-1,n,re,str1,ans)
    else:
        return ans

    
    
for _ in range(int(input())):
    str1=input()
    str2=input()
    a=[[-1]*(len(str1)+1) for _ in range(len(str2)+1)]
    re=[[-1]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(len(str1)+1):
        a[0][i]=0
    for i in range(len(str2)+1):
        a[i][0]=0
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if(str2[i-1]==str1[j-1]):
                
                a[i][j]=1+a[i-1][j-1]
                re[i][j]=1
                
            else:
                
                a[i][j]=max(a[i-1][j],a[i][j-1])
                if(a[i][j]==a[i][j-1]):
                    re[i][j]=0
                else:
                    re[i][j]=2


    w=display(a,len(str2),len(str1),re,str2,[])
    w.reverse()
    print("".join(str(i) for i in w))
