n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
for i in range(n-1):
    for j in range(len(arr[i])):
        dp[i+1][j]=max(dp[i+1][j],arr[i+1][j]+arr[i][j])
        dp[i+1][j+1]=max(dp[i+1][j+1],arr[i+1][j+1]+arr[i][j])
    for j in range(len(arr[i+1])):
        arr[i+1][j]=dp[i+1][j]
if n==1:
    print(arr[0][0])
else:
    print(max(dp[-1]))