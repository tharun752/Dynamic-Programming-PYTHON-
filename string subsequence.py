def subsequence(strs,re,ex,index):
    if(index==len(strs)):
        re.append(ex)
        return 
    subsequence(strs,re,ex,index+1)
    subsequence(strs,re,ex+strs[index],index+1)

for _ in range(int(input())):
    strs=input()
    re=[]
    subsequence(strs,re,"",0)
    cnt={}
    for i in re:
        cnt[i]=cnt.get(i,0)+1


    mx=-1
    for i in cnt:
        if(cnt[i]>mx):
            mx=cnt[i]
    print(mx-1)
