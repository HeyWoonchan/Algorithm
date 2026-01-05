n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [[0,0] for _ in range(n)]
#이전 계단을 밟고 올라온 경우[1]/안밟고 올라온 경우[0]
dp[0]=[arr[0],arr[0]]
if n>1:
    dp[1][1]=arr[0]+arr[1]
    dp[1][0]=arr[1]

for i in range(2,n):
    dp[i][1]=arr[i]+dp[i-1][0]
    dp[i][0]=arr[i]+max(dp[i-2])
print(max(dp[n-1]))