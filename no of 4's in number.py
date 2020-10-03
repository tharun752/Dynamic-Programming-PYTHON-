def countNumberswith4( N):
        re=0
        for i in range(N+1):
            re+=fun(i)
        return re
        # code here
def fun(n):
    cnt=0
    while(n>0):
        k=n%10
        if(k==4):
            cnt+=1
        n//=10
    return cnt
print(countNumberswith4(24))