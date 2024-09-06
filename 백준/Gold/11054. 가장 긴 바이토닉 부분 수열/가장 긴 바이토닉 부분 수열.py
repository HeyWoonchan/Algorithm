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

dp2 = [0]* len(arr); dp2[-1]=1
for i in range(len(arr)-1,-1,-1):
    tmp=0
    for j in range(len(arr)-1,i-1,-1):
        if arr[i]>arr[j]:
            tmp = max(tmp,dp2[j])
    dp2[i]=tmp+1
ans = 0


for i in range(len(arr)):
    ans = max(ans, dp[i]+dp2[i]-1)

# print(dp)
# print(dp2)

print(ans)