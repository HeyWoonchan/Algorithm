import sys
from collections import deque
input =sys.stdin.readline
N,M=map(int,input().split())
graph=[[]for _ in range(N+1)]

for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    q=deque([node])
    visited[node]=1
    while q:
        node=q.popleft()
        for nextNode in graph[node]:
            if visited[nextNode]==0:
                visited[nextNode]=1
                q.append(nextNode)
visited=[0]*(N+1)
ans=0
for i in range(1,N+1):
    if visited[i]==0:
        bfs(i)
        ans+=1
print(ans)