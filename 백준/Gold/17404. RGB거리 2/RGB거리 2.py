#처음에 뭐골라서 온건지만 체크?
"""
RGB거리_2의 Docstring

위아래도 맞지 않아야 하고, 
그러면서 최소 비용 구하기
2<=N<=1000
무조건 최소 비용만 선택한다면,
색을 위아래와 무조건 다르게 선택해야한다는 조건
때문에 최적 답이 아닐 수 있음.

dp[i][0][n] = min(dp[i-1][1][n],dp[i-1][2][n])+arr[i][0]



26 40 83
49 60 57
13 89 99
26 40 83

마지막만 체크하면 됨.
첫번째에서 뭐가 기록되어 넘어왔는지
마지막에서, 이전에서 넘어온 것이 
첫번째에서 같은 것을 체크했다면 고를 수 없음.


->dp[i][0][n] = min(dp[i-1][1][n],dp[i-1][2][n])+arr[i][0]
dp[i][0][n] = 첫번째가 n인 i-1의 다른 두 개 중 가장 작은 것.

"""
import sys
input = sys.stdin.readline
N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]
INF = float('inf')

dp = [[[INF]*3 for _ in range(3)] for _ in range(N)]
ans = INF
for i in range(N):
    if i==0:
        # if arr[0][1]>arr[0][2]:
        #     dp[i][0][2] = arr[0][2]+arr[i][0]
        # elif arr[0][1]<arr[0][2]:
        #     dp[i][0][1] = arr[0][1]+arr[i][0]
        # else:
        #     dp[i][0][1] = arr[0][1]+arr[i][0]
        #     dp[i][0][2] = arr[0][2]+arr[i][0]
        # for j in range(3):
        dp[i][0][0] = arr[i][0]
        dp[i][1][1] = arr[i][1]
        dp[i][2][2] = arr[i][2]
        continue
    if i==N-1:
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if j==k or j==l:
                        continue
                    # print(j,k,l,dp[i-1][k][l])
                    ans = min(ans, arr[i][j]+dp[i-1][k][l])
        
    for j in range(3):
        dp[i][0][j] = arr[i][0]+min(dp[i-1][1][j], dp[i-1][2][j])
        dp[i][1][j] = arr[i][1]+min(dp[i-1][0][j], dp[i-1][2][j])
        dp[i][2][j] = arr[i][2]+min(dp[i-1][0][j], dp[i-1][1][j])
    

# print(*dp, sep='\n')
print(ans)