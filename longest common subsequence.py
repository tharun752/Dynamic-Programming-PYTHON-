def lcs(i,j,str1,str2,arr):
    if(arr[i][j]!=-1):
        return arr[i][j]
    if(i<=0 or j<=0):
        return 0
   
    
    if(str1[i-1]==str2[j-1]):
        arr[i][j]= 1+lcs(i-1,j-1,str1,str2,arr)
    else:
        arr[i][j]= max(lcs(i-1,j,str1,str2,arr),lcs(i,j-1,str1,str2,arr))
    
    return arr[i][j]
    
    
    
for _ in range(int(input())):
    i,j=map(int,input().split())
    str1=input()
    str2=input()
    l=[[-1]*(j+1) for _ in range(i+1)]
    
    for m in range(i+1):
        for n in range(j+1): 
            if(m==0 or n==0):
                
                l[m][n]=0
    
        
    print(lcs(i,j,str1,str2,l))