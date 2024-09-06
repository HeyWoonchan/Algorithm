N = int(input())
arr = list(map(int,input().split()))

dp = [0]*len(arr)
dp[0]=1
for i in range(len(arr)):
    tmp=0
    for j in range(i):
        if arr[i]>arr[j]:
            tmp = max(tmp,dp[j])
    dp[i]=tmp+1

# print(dp)
print(max(dp))