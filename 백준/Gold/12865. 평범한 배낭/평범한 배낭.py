N,K=map(int,input().split())
things=[(0,0)]+[tuple(map(int,input().split())) for _ in range(N)]

#넣거나 안넣거나
#dp[i][j] i번째 물건까지 넣고, j무게까지 넣었을 때의 최대 가치
dp=[[0]*(K+1) for _ in range(N+1)]
# print(things)
for i in range(1,N+1): 
    w,v = things[i]
    # print("물건i:",i,"w,v:",w,v)
    for j in range(K+1):
        # print("j:",j)
        if w>j:
            # print("w>j")
            dp[i][j]=dp[i-1][j]
        else:
            # print("w<=j")
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        # print(dp[i][j])
    # print(*dp,sep='\n')
    



# print(dp)
print(dp[i][K])