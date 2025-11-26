N = int(input())

dp = [[0]*(N+1) for _ in range(10)]
MOD = 1000000000

for i in range(1,10):
    dp[i][1]=1

for j in range(2,N+1):
    for i in range(0,10):
        if i-1>=0:
            dp[i][j] += dp[i-1][j-1]
        if i+1<10:
            dp[i][j] += dp[i+1][j-1]
        dp[i][j]%=MOD

answer = 0
for i in range(10):
    answer+=dp[i][N]
print(answer%MOD)
