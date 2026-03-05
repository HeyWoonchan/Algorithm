import sys, heapq
input = sys.stdin.readline
INF = float('inf')
N, E = map(int,input().split())
graph =[[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())



def dijkstra(start, end):
    hq = [(0,start)]
    dist = [INF]*(N+1)

    while hq:
        nowCost, nowNode = heapq.heappop(hq)

        if dist[nowNode]<nowCost:
            continue

        for nextNode, nextCost in graph[nowNode]:
            newCost = nowCost+nextCost

            if dist[nextNode]>newCost:
                dist[nextNode]=newCost
                heapq.heappush(hq,(newCost,nextNode))
    
    return dist[end]
if v1==1:
    oneTov1=0
else:
    oneTov1 = dijkstra(1,v1)
v1Tov2 = dijkstra(v1,v2)
v2Tov1 = dijkstra(v2,v1)
ontTov2 = dijkstra(1,v2)
v1ToN = dijkstra(v1,N)
if v2==N:
    v2ToN=0
else:
    v2ToN = dijkstra(v2,N)

#1->v1->v2->N
firstOption = oneTov1+v1Tov2+v2ToN

#1->v2->v1->N
secondOption = ontTov2+v2Tov1+v1ToN
ans = min(firstOption,secondOption)
print(ans if ans != INF else -1)