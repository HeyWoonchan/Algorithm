N, K = map(int, input().split())

arr = [(0,0)]+[tuple(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    weight, value = arr[i]
    for j in range(K+1):
        if weight>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[N][K])