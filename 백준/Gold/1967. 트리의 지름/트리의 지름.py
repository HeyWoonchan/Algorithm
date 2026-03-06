import heapq
INF = float('inf')
n = int(input())

graph = [[] for _ in range((n+1))]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    hq= [(0,start)]
    dist = [INF]*(n+1)
    dist[start]=0

    while hq:
        nowCost, nowNode = heapq.heappop(hq)
        
        if dist[nowNode]<nowCost:
            continue

        for nextNode, nextCost in graph[nowNode]:
            newCost = nowCost+nextCost

            if dist[nextNode]>newCost:
                dist[nextNode] = newCost
                heapq.heappush(hq, (newCost,nextNode))

    return dist

first = dijkstra(1)
findFirstMax = [ ]
for i in range(0,n+1):
    if first[i]==INF:
        continue
    findFirstMax.append((first[i],i))
findFirstMax.sort()
second = dijkstra(findFirstMax[-1][1])
secondMax = 0
for j in second:
    if j!=INF:
        secondMax = max(secondMax,j)
print(secondMax)
