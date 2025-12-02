from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
mat = []
zeromap = [[0]*M for _ in range(N)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(N):
    a = input()
    mat.append(a)

def bfs(r,c, visited):
    q = deque([(r,c)])
    visited[r][c]=1
    zeroNum = 0
    wallToAdd = []
    while q:
        r, c = q.popleft()
        zeroNum+=1
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if not (0<=nr<N and 0<=nc<M):
                continue
            if visited[nr][nc]==0:
                if mat[nr][nc]=='0':
                    q.append((nr,nc)) 
                else:
                    wallToAdd.append((nr,nc))
                visited[nr][nc]=1

    #만나는 벽에 0영역 넓이를 더해주고, 이 벽의 경우 다음번에 또 탐색 되어야 하므로 방문 초기화
    for r, c in wallToAdd:
        answerMap[r][c]+=zeroNum
        visited[r][c]=0

visited = [[0]*M for _ in range(N)] 
answerMap = [[0]*M for _ in range(N)]
closedMap = [[0]*M for _ in range(N)]

#0인 곳에 각각의 넓이를 기록+만나는 벽에 0의 넓이를 더해줌
#벽이 상하좌우로 막힌 경우, 그곳은 무조건 1로 처리 해줘야함.
for i in range(N):
    for j in range(M):
        if visited[i][j]==1:
            continue
        if mat[i][j]=='0':
            bfs(i,j,visited)
        else:
            near = 0
            for dr, dc in d:
                nr, nc = i+dr, j+dc
                if not (0<=nr<N and 0<=nc<M):
                    continue
                if mat[nr][nc]=='0':
                    near+=1
            if near==0:
                closedMap[i][j]=1
                answerMap[i][j]=1

for i in range(N):
    for j in range(M):
        if mat[i][j]=='1' and closedMap[i][j]==0:
            answerMap[i][j]+=1
            answerMap[i][j]%=10


for i in range(N):
    for j in range(M):
        print(answerMap[i][j], end='')
    print()
