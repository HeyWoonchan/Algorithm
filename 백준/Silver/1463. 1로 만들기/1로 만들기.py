X = int(input())

dp=[float('inf')]*(10**6+1)
dp[1]=0

for i in range(1,len(dp)-1):
    dp[i+1]=min(dp[i+1],dp[i]+1)
    if i*2<len(dp):
        dp[i*2]=min(dp[i*2],dp[i]+1)
    if i*3<len(dp):
        dp[i*3]=min(dp[i*3],dp[i]+1)

print(dp[X])