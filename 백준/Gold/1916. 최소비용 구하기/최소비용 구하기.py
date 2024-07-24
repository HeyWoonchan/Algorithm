import sys,heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    adj_list[s].append((e,c))
start, end = map(int,input().split())

INF = float('inf')
def dijkstra(start, end):
    dist = [INF]*(N+1)
    dist[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        nowcost, nownode = heapq.heappop(q)
        if dist[nownode]<nowcost:
            continue
        for nextnode, nextcost in adj_list[nownode]:
            tmp_cost = nowcost+nextcost
            if dist[nextnode]>tmp_cost:
                dist[nextnode]=tmp_cost
                heapq.heappush(q, (tmp_cost,nextnode))
    return dist[end]

print(dijkstra(start,end))

