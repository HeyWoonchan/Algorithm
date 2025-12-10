N = int(input())
W=[list(map(int,input().split())) for _ in range(N)]

"""
어차피 최솟값을 이루는 cycle은
어떤 노드에서 출발하는 경로여도 같은 cycle 한 종류이기 때문에 출발을 0으로 고정.

dp[nownode][visitedMask(2)] = 0부터 출발해서, nownode까지 왔을때, 
방문점은 visitedMask(2)인 상태에서, 방문 안한 나머지 것들을 순회하는 모든 경우 중 최소 비용
dp[-][모든노드 방문 완료 mask(1<<N -1)]에서부터 역방향으로 채워짐
"""

MASK = int("0b"+"1"*N,0)
INF = float('inf')

dp = [[-1]*MASK for _ in range(N)]



def dfs(nowNode,mask):

    # print("now visiting:", nowNode, mask)
    if mask == MASK:
        if W[nowNode][0]==0:
            return INF
        else:
            return W[nowNode][0]
    

    if dp[nowNode][mask]!=-1: #memoization
        return dp[nowNode][mask]
    dp[nowNode][mask]=INF #못가는 곳과, 탐색하지 않은 곳을 구별해야 함.
    
    
    for nextNode in range(N):
        if W[nowNode][nextNode]==0:
            continue
        if (mask&(1<<nextNode))==0:
            cost = W[nowNode][nextNode] + dfs(nextNode, mask | (1<<nextNode))
            dp[nowNode][mask] = min(dp[nowNode][mask], cost)
    return dp[nowNode][mask]


dp[0][1] = dfs(0,1)

# print(dp)
print(dp[0][1])