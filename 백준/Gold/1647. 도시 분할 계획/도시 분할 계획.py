#MST 
import heapq, sys
input = sys.stdin.readline

N, M = map(int,input().split())
connect = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int,input().split())
    connect[A].append((B, C))
    connect[B].append((A, C))

selectedCostSum = 0
selectedCostMax = 0
selectedEdgeCnt = 0

#prim알고리즘
#1번 정점을 시작으로(어떤 것으로 시작해도 상관 없음), 간선을 힙에 넣어주고
#가장 작은 간선을 뽑고, 간선이 연결된 정점에 연결된 간선을 힙에 넣어줌(이미 선택한 노드라면 넣지 않음)
#이제, 힙에 넣은 것 중에서 제일 작은 간선을 뽑음 -> 뽑은 간선이 N-1개가 될 때 까지 반복
#바로 이전에서 넣은 것일 수도 있고, 좀 더 전에 넣었던 것이 뽑힐 수도 있다는 점에 유의

edges = []
selectedNodes = [0]*(N+1)

selectedNodes[1]=1
for node, cost in connect[1]:
    heapq.heappush(edges, (cost, node))

while selectedEdgeCnt<N-1:
    cost, node = heapq.heappop(edges)
    if selectedNodes[node]==1: #중요 - 맨처음에 넣었던 것중에서도 이걸 체크 안하고 뽑힐수도 있기때문에 반드시 필요
        continue
    selectedNodes[node]=1
    selectedEdgeCnt+=1
    selectedCostSum += cost
    selectedCostMax = max(selectedCostMax, cost)
    for nextNode, nextCost in connect[node]:
        if selectedNodes[nextNode]==1:
            continue
        heapq.heappush(edges, (nextCost, nextNode))

print(selectedCostSum-selectedCostMax)