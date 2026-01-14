from collections import deque
N=int(input())
grid=[input() for _ in range(N)]
d=[(1,0),(0,1),(-1,0),(0,-1)]



visited=[[0]*N for _ in range(N)]
def normalBfs(i,j):
    q=deque()
    q.append((i,j))
    visited[i][j]=1
    while q:
        r,c=q.popleft()
        for dr,dc in d:
            nr,nc=r+dr,c+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            if grid[r][c]==grid[nr][nc] and visited[nr][nc]==0:
                visited[nr][nc]=1
                q.append((nr,nc))
def rgBfs(i,j):
    q=deque()
    q.append((i,j))
    visited[i][j]=1
    while q:
        r,c=q.popleft()

        for dr,dc in d:
            nr,nc=r+dr,c+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            if (grid[r][c]==grid[nr][nc] or (grid[r][c],grid[nr][nc])==('R','G') or (grid[r][c],grid[nr][nc])==('G','R'))  and visited[nr][nc]==0:
                visited[nr][nc]=1
                q.append((nr,nc))
normalCnt=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            normalBfs(i,j)
            normalCnt+=1

visited=[[0]*N for _ in range(N)]
rgCnt=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            rgBfs(i,j)
            rgCnt+=1

print(normalCnt,rgCnt)