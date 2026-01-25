N,K=map(int,input().split())
things=[tuple(map(int,input().split())) for _ in range(N)]

#넣거나 안넣거나
dp=[0]*(K+1)

for w, v in things:
    for j in range(K,w-1,-1):
        dp[j]=max(dp[j],dp[j-w]+v)
print(dp[K])