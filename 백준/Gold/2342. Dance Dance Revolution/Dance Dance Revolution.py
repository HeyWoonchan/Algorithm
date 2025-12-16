import sys
input = sys.stdin.readline

query = list(map(int,input().split()))
query.pop()
INF = float("inf")
"""
한쪽 발이 선택되었다면, 다른 한쪽발은 가만히
한번 한 사고과정을 또 하지 않도록, 사고의 흐름을 반드시 기록
0,0으로 말단에 기록한다면, 이전 단계에서는 왼발이 이동한 경우, 
오른발이 이동한 경우 모두에 대해 기록할 수 있나?
결국에 다음 점수로, 왼발이 이동하냐, 오른발이 이동하냐이다.
지금단계(왼발, 오른발) = 이전단계에서 왼발이 이동한 경우, 오른발이 이동한 경우.
-> 마지막단계에서, 이전단계 중, 왼발이 넘어온 경우와, 오른발이 넘어온 경우 중 최소.
그렇다면 지금단계를 어떻게 점화식을 세워야 하는가?
dp[i][(1,0)] = 왼발 ->dp[i-1][(0,0),(2,0),(3,0),(4,0)] / 오른발(0이므로 0에서만 올 수 있음)->dp[i-1][(1,0)] 중 최소
dp[i][(query[i],0)]
dp[i][query[i]][j], query[i] = min( (dp[i-1][0~4 =k][query[i]], k!=query[i]), ())
dp[i][]
최종 답: 마지막 query가 4라면, dp[len(query)-1][(4,0),(4,1),(4,2),(4,3),(0,4),(1,4),(2,4),(4,2)]중 가장 적은 값

1
0,0에서, 왼쪽발로 이동한 경우->1,0
0,0에서, 오른쪽발로 이동한 경우->0,1

2
1,0에서, 왼쪽발로 이동한 경우->2,0
1,0에서, 오른쪽발로 이동한 경우->1,2
0,1에서, 왼쪽발로 이동한 경우->2,1
0,1에서, 오른쪽발로 이동한 경우,0,2

2
2,0에서, 왼쪽발로 이동한 경우->2,0
2,0에서, 오른족발로 이동할 수 없음>x
1,2에서, 


general
0->처음에만 목표로 가능

1
0,0->1,0
0,0->0,1
0,1->0,1
0,1->1,1->x
0,2->1,2
0,2->0,1
0,3->1,3
0,3->0,1
0,4->1,4
0,4->0,1
1,2->1,2
1,2->1,1->x
1,3->1,3
1,3->1,1->x
1,4->1,4
1,4->1,1->x
2,1->1,1->x
2,1->2,1
2,3->1,3
2,3->2,1
2,4->1,4
2,4->2,1
3,1->1,1->x
3,1->3,1
3,2->1,2
3,2->3,1
3,4->1,4
3,4->3,1
4,1->1,1->x
4,1->4,1
4,2->1,2
4,2->4,1
4,3->1,3
4,3->4,1



2
3
4

이전 단계에서 움직일 수 있었던 자리만 허용 필요

"""
dp = [[[INF]*5 for _ in range(5)] for _ in range(len(query)+1)]
dp[0][0][0]=0
for q in range(len(query)):

    # print("q:",query[q])
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
                # print("adding",i,j,"to",i,k,"add:",adding,dp[q+1][i][k])

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
                # print("adding",i,j,"to",k,j,"add:",adding,dp[q+1][k][j] )

ans = INF
for i in range(5):
    for j in range(5):
        ans = min(ans,dp[len(query)][i][j])
print(ans)

# print(*dp,sep='\n')