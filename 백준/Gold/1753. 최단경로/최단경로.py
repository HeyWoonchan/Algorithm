import heapq
from collections import deque
import sys

V, E = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(V+1)]
start_node = int(input())

for _ in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    adj_list[u].append((v,w))
INF = 1e9
def dijkstra(start):
    dist = [INF]*(V+1)
    dist[start]=0
    min_heap = []
    heapq.heappush(min_heap,(0,start)) # (weight, node)
    
    while min_heap:
        now_weight, now_node = heapq.heappop(min_heap)
        if dist[now_node]<now_weight:
            continue
        for next_node, next_weight in adj_list[now_node]:
            tmp_weight = now_weight+next_weight
            if tmp_weight<dist[next_node]:
                dist[next_node] = tmp_weight
                heapq.heappush(min_heap,(tmp_weight, next_node))
    return dist

dist = dijkstra(start_node)



# def bfs(start):
    
#     q = deque([(start,0)])
#     dist= [INF]*(V+1)
#     dist[start]=0
    
#     #바로 전것만 다시 안가면 됨
#     visited = [0]*(V+1)
#     visited[start]=1
#     while q:
#         nownode, nowweight = q.popleft()
#         # print(q)
#         # print("현재노드:",nownode, nowweight)
#         dist[nownode] = min(dist[nownode], nowweight)
#         # print(dist)
#         visited[nownode]=1
#         # print("현재 노드에서 갈 수 있는 길:",adj_list[nownode])
#         for nextnode , nextweight in adj_list[nownode]:
#             # print("다음노드삽입",nextnode,nextweight)    
#             if visited[nextnode]==1:
#                 # print("불가!!")
#                 continue
#             q.append((nextnode, nowweight+nextweight))

#     return dist



dist = dijkstra(start_node)
for i in range(1, V+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])