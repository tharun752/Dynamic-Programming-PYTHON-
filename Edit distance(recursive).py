def oper(str1,str2,m,n):
    if(m==0):
        return n
    if(n==0):
        return m
    if(str1[m-1]==str2[n-1]):
        return oper(str1,str2,m-1,n-1)
    else:
        return 1+min(oper(str1,str2,m-1,n),oper(str1,str2,m,n-1),oper(str1,str2,m-1,n-1))
for _ in range(int(input())):
    str1=input()
    str2=input()
    print(oper(str1,str2,len(str1),len(str2)))