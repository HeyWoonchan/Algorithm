MAXINT = 1000001
nums = [1]*MAXINT
nums[1]=0
for i in range(2,MAXINT):
    for j in range(i*2,MAXINT,i):
        nums[j]=0
n,m = map(int,input().split())
for i in range(n,m+1):
    if nums[i]==1:
        print(i)