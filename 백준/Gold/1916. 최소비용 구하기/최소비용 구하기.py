import sys,heapq
input= sys.stdin.readline
INF = float('inf')
N = int(input())
M=int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    U,V,cost = map(int,input().split())
    graph[U].append((V,cost))
start, end = map(int,input().split())

dist = [INF]*(N+1)

hq = [(0,start)]
while hq:
    nowDist, nowNode = heapq.heappop(hq)
    if dist[nowNode]<nowDist:
        continue
    for nextNode, cost in graph[nowNode]:
        if nowDist+cost<dist[nextNode]:
            dist[nextNode]=nowDist+cost
            heapq.heappush(hq, (nowDist+cost, nextNode))

print(dist[end])