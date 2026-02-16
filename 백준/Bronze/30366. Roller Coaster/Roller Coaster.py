N,M = map(int,input().split())
arr = list(map(int,input().split()))
nowSum = 0
time = [0]*N
t = 0
for i in range(N):
    if nowSum+arr[i]>M:
        nowSum=arr[i]
        t+=1
        time[i]=t
    else:
        time[i]=t
        nowSum+=arr[i]
for a in time:
    print(a)