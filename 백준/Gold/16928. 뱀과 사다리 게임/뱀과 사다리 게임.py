from collections import deque
N,M=map(int,input().split())
ladders=[0]*101
snakes=[0]*101
for _ in range(N):
    x,y=map(int,input().split())
    ladders[x]=y
for _ in range(M):
    u,v=map(int,input().split())
    snakes[u]=v

q=deque([(1,0)])
visited=[0]*101
visited[1]=1
while q:
    u,cnt=q.popleft()
    if u==100:
        print(cnt)
        exit(0)
    for i in range(1,7):
        v=u+i
        if not v<101:
            continue
        if ladders[v]!=0:
            v=ladders[v]
        if snakes[v]!=0:
            v=snakes[v]
        if visited[v]==0:
            visited[v]=1
            q.append((v,cnt+1))
