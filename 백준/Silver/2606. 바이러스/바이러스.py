from collections import deque
n=int(input())
e=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[0]*(n+1)
q = deque([1])
visited[1]=1
ans=0
while q:
    u = q.popleft()
    if u!=1:
        ans+=1
    for v in graph[u]:
        if visited[v]==0:
            q.append(v)
            visited[v]=1
print(ans)

