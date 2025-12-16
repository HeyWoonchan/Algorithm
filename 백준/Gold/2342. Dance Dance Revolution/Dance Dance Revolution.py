import sys
input = sys.stdin.readline

query = list(map(int,input().split()))
query.pop()
INF = float("inf")
dp = [[[INF]*5 for _ in range(5)] for _ in range(len(query)+1)]
dp[0][0][0]=0
for q in range(len(query)):
    for i in range(5):
        for j in range(5):
            if i==j and i!=0:
                continue
            if dp[q][i][j]==INF:
                continue
            for k in range(5):
                if k!=query[q]:
                    continue
                if i==k:
                    continue
                adding = 0
                if j==0:
                    adding=2
                elif abs(k-j)==1 or abs(k-j)==3:
                    adding=3
                elif abs(k-j)==2:
                    adding=4
                else:
                    adding=1
                dp[q+1][i][k] = min(dp[q+1][i][k],dp[q][i][j] + adding )
            for k in range(5):
                if k!=query[q]:
                    continue
                if k==j:
                    continue
                
                adding = 0
                if i==0:
                    adding=2
                elif abs(k-i)==1 or abs(k-i)==3:
                    adding=3
                elif abs(k-i)==2:
                    adding=4
                else:
                    adding=1
                
                dp[q+1][k][j] = min(dp[q+1][k][j],dp[q][i][j] + adding)


ans = INF
for i in range(5):
    for j in range(5):
        ans = min(ans,dp[len(query)][i][j])
print(ans)
