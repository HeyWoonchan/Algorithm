from collections import deque
TC = int(input())

def bfs(r,c):
    visited[r][c]=1
    q=deque([(r,c)])
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        r,c = q.popleft()
        for dr, dc in d:
            nr,nc = r+dr, c+dc
            if not (0<=nr<N and 0<=nc<M):
                continue
            if graph[nr][nc]==1 and visited[nr][nc]==0:
                visited[nr][nc]=1
                q.append((nr,nc))
    
for _ in range(TC):
    M,N,v=map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(v):
        x,y=map(int,input().split())
        graph[y][x]=1
    # print(graph)
    visited=[[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and visited[i][j]==0:
                bfs(i,j)
                cnt+=1
    print(cnt)