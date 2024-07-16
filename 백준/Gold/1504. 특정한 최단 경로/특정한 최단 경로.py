import heapq
N, E = map(int, input().split())

adj_list = [[] for _ in range(N)]
for _ in range(E):
    a,b,c = map(int, input().split())
    adj_list[a-1].append((b-1,c))
    adj_list[b-1].append((a-1,c))

v1, v2 = map(int, input().split())

# solution for 1 -> N, must visit v1 and v2
# revisiting nodes and edges is possible
"""
v1, v2정점을 거치는 최단경로
1->v1->v2->N
1->v2->v1->N?
"""
INF = int(1e9)
def dijkstra(start):
    dist = [INF]*N
    dist[start]=0
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        nowdist, nownode = heapq.heappop(pq)
        for node, edge in adj_list[nownode]:
            tmp_dist = nowdist+edge
            if tmp_dist<dist[node]:
                heapq.heappush(pq,(tmp_dist,node))
                dist[node]=tmp_dist
    return dist

dist0=dijkstra(0)
distv1=dijkstra(v1-1)
distv2=dijkstra(v2-1)
v1tov2 = dist0[v1-1]+distv1[v2-1]+distv2[N-1]
v2tov1 = dist0[v2-1]+distv2[v1-1]+distv1[N-1]
if v1tov2>=INF and v2tov1>=INF:
    print(-1)
else:
    print(min(v1tov2,v2tov1))
