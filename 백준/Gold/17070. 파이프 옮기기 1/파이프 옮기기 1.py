N = int(input())
marr = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0,0,0] for _ in range(N+1)] for _ in range(N+1)]

# state 0:가로, 1:세로, 2:대각선
dp[1][2][0]=1
# print(dp)
# print()
for i in range(N+1):
    for j in range(1,N+1):
        if (i,j)==(1,2):
            continue
        if marr[i-1][j-1]==1:
            continue
        dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2]
        dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2]
        if marr[i-2][j-1]== 0 and marr[i-1][j-2]==0:
            dp[i][j][2]=sum(dp[i-1][j-1])

print(sum(dp[N][N]))