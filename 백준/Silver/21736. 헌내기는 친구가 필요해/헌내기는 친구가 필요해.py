import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
grid=[input() for _ in range(N)]

def bfs(r,c):
    visited=[[0]*M for _ in range(N)]
    d=[(0,1),(1,0),(-1,0),(0,-1)]
    q=deque([(r,c)])
    visited[r][c]=1
    met=0
    while q:
        r,c=q.popleft()
        if grid[r][c]=='P':
            met+=1
        for dr,dc in d:
            nr,nc=r+dr,c+dc
            if not (0<=nr<N and 0<=nc<M):
                continue
            if grid[nr][nc]!='X' and visited[nr][nc]==0:
                visited[nr][nc]=1
                q.append((nr,nc))
    return met 


for i in range(N):
    for j in range(M):
        if grid[i][j]=='I':
            ans=bfs(i,j)
            if ans==0:
                print("TT")
            else:
                print(ans)
            exit(0)