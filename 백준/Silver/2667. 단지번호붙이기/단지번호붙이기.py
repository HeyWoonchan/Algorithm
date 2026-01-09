from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
grid=[input() for _ in range(N)]

ans=[]
visited=[[0]*N for _ in range(N)]

def bfs(r,c):
    d=[(0,1),(1,0),(-1,0),(0,-1)]
    q=deque([(r,c)])
    visited[r][c]=1
    cnt=0
    while q:
        r,c=q.popleft()
        cnt+=1
        for dr,dc in d:
            nr,nc=r+dr,c+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            if grid[nr][nc]=='1' and visited[nr][nc]==0:
                visited[nr][nc]=1
                q.append((nr,nc))
    return cnt


for i in range(N):
    for j in range(N):
        if grid[i][j]=='1' and visited[i][j]==0:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans))
print(*ans,sep='\n')