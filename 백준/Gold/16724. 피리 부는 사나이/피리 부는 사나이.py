import sys
from collections import deque

N, M = map(int,input().split())
board = [input() for _ in range(N)]


def bfs(r,c,visited):
    q = deque([(r,c)])
    #내쪽을 바라보고 있거나, 내 화살표가 가리키는 방향 고려해서 그 영억에 하나만 있으면 됨
    visited[r][c]=1
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        r, c = q.popleft()
        # print(r,c)
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if not (0<=nr<N and 0<=nc<M):
                continue
            if visited[nr][nc]==1:
                continue
            if (dr,dc)==(0,1) and board[nr][nc]=='L':
                q.append((nr,nc))
                visited[nr][nc]=1
            elif (dr,dc)==(0,-1) and board[nr][nc]=='R':
                q.append((nr,nc))
                visited[nr][nc]=1
            elif (dr,dc)==(1,0) and board[nr][nc]=='U':
                q.append((nr,nc))
                visited[nr][nc]=1
            elif (dr,dc)==(-1,0) and board[nr][nc]=='D':
                q.append((nr,nc))
                visited[nr][nc]=1

        if board[r][c]=='L' and 0<=c-1 and visited[r][c-1]==0:
            q.append((r,c-1))
            visited[r][c-1]=1
        elif board[r][c]=='R' and c+1<M and visited[r][c+1]==0:
            q.append((r,c+1))
            visited[r][c+1]=1
        elif board[r][c]=='U' and 0<=r-1 and visited[r-1][c]==0:
            q.append((r-1,c))
            visited[r-1][c]=1   
        elif board[r][c]=='D' and r+1<N and visited[r+1][c]==0:
            q.append((r+1,c))
            visited[r+1][c]=1

visited = [[0]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]==0:
            # print("탐색시작", i,j)
            bfs(i,j,visited)
            cnt+=1
            # print()

print(cnt)
        
