def knapsack(weight,weights,values,n):
    if(n==0 or weight==0):
        return 0
    if(weight<weights[n-1]):
        return knapsack(weight,weights,values,n-1)
    else:
        return max((values[n-1]+knapsack(weight-weights[n-1],weights,values,n-1)),knapsack(weight,weights,values,n-1))
for _ in range(int(input())):
    weights=list(map(int,input().split()))
    values=list(map(int,input().split()))
    weight=int(input())
    print(knapsack(weight,weights,values,len(weights)))