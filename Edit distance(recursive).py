
for _ in range(int(input())):
    str1=input()
    str2=input()
    d=[[-1]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(len(str1)+1):
        d[0][i]=i
        d[i][0]=i
    
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if(str2[i-1]==str1[j-1]):
                d[i][j]=d[i-1][j-1]
            else:
                d[i][j]=1+min(d[i][j-1],d[i][j-1],d[i-1][j-1])
    print(d[len(str2)][-1])