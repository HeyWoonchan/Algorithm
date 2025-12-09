first = input().rstrip()
second = input().rstrip()

dp=[[0]*(len(second)+1) for _ in range(len(first)+1)]

ans = 0
for i in range(1,len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1]==second[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1], dp[i-1][j])
        ans = max(ans,dp[i][j])
print(ans)
