from collections import deque

def setTimeWallExit():
    leftUpR, leftUpC = -1,-1
    for r in range(N):
        if leftUpC!=-1:
            break
        for c in range(N):
            if floorBoard[r][c]==3:
                leftUpR, leftUpC = r,c
                break

    for r in range(N):
        for c in range(N):
            if floorBoard[r][c]==3:
                if floorBoard[r][c+1]==0:
                    cubeBoardTri[0][M-1][M-1-(r-leftUpR)]=3
                    return r,c+1
                elif floorBoard[r-1][c]==0:
                    cubeBoardTri[1][M-1][M-1-(c-leftUpC)]=3
                    return r-1,c
                elif floorBoard[r][c-1]==0:
                    cubeBoardTri[2][M-1][r-leftUpR]=3
                    return r,c-1
                elif floorBoard[r+1][c]==0:
                    cubeBoardTri[3][M-1][c-leftUpC]=3
                    return r+1,c

def findTimeWallExit():
    # 1. 맨윗단에서 우주선 찾기
    shipR, shipC = -1,-1
    for r in range(M):
        if shipC!=-1:
            break
        for c in range(M):
            if cubeBoardTri[4][r][c]==2:
                shipR,shipC = r,c
                break

    #bfs시작
    visited = [[[0]*M for _ in range(M)] for _ in range(5)]
    visited[4][shipR][shipC]=1
    q = deque()
    q.append((4,shipR,shipC,0))
    while q:
        i,j,k, cnt= q.popleft()
        if cubeBoardTri[i][j][k]==3:
            return cnt
        for dr, dc in [(0,-1),(0,1),(1,0),(-1,0)]:
            nr,nc = j+dr,k+dc
            if (0<=nr<M and 0<=nc<M):
                dir = i 
            else:
                if i==4: #윗면에서 넘어간경우
                    if nr<0:
                        dir = 1
                        nr = 0
                        nc = M-1-nc
                    elif nr>=M:          
                        dir = 3
                        nr = 0
                        nc = nc                       
                    elif nc<0:
                        dir = 2
                        nc = nr
                        nr = 0
                    elif nc>=M:
                        dir = 0
                        nc = M-1-nr
                        nr=0
                elif i==0: #옆면에서 넘어간경우
                    if nr<0:
                        dir = 4
                        nr = M-1-nc
                        nc = M-1
                    elif nr>=M: #아래방향 x
                        continue
                    elif nc<0:
                        dir = 3
                        nr = nr
                        nc = M-1
                    elif nc>=M:
                        dir = 1
                        nc = 0
                        nr= nr
                elif i==1:
                    if nr<0:
                        dir = 4
                        nr = nc
                        nc = 0
                    elif nr>=M: #아래방향 x
                        continue
                    elif nc<0:
                        dir = 0
                        nr = nr
                        nc = M-1
                    elif nc>=M:
                        dir = 2
                        nc = 0
                        nr= nr
                elif i==2:
                    if nr<0:
                        dir = 4
                        nr = 0
                        nc = M-1-nc
                    elif nr>=M: #아래방향 x
                        continue
                    elif nc<0:
                        dir = 1
                        nr = nr
                        nc = M-1
                    elif nc>=M:
                        dir = 3
                        nc = 0
                        nr= nr
                elif i==3:
                    if nr<0:
                        dir = 4
                        nr = M-1
                        nc = nc
                    elif nr>=M: #아래방향 x
                        continue
                    elif nc<0:
                        dir = 2
                        nr = nr
                        nc = M-1
                    elif nc>=M:
                        # print("3->0", i,nr,nc)
                        dir = 0
                        nc = 0
                        nr= nr
            if visited[dir][nr][nc]==0 and cubeBoardTri[dir][nr][nc]!=1:
                visited[dir][nr][nc]=1
                q.append((dir,nr,nc,cnt+1))
                    
    return -1

def findUnSpaceExit(timeWallDuration, floorStartR,floorStartC):
    # 시간의 벽에서 경과된 시간만큼
    # 이상현상 진행
    # 초기 이상현상은 0초에 모두 이미 진행
    # 새로 맵 만들어서, 초별로 어디에 생기는지 모두 기록
    # 기본 = -1

    abnomalEffectBoard = [[-1]*N for _ in range(N)]
    dList = [(0,1),(0,-1),(1,0),(-1,0)]
    
    for i in range(F):
        r,c,d,v = abnomalEffect[i]
        
        abnomalEffectBoard[r][c]= 0
        time = v
        
        while True:
            dr,dc = dList[d]
            nr,nc = r+dr,c+dc
            if not (0<=nr<N and 0<=nc<N):
                break
            if floorBoard[nr][nc]==1 or floorBoard[nr][nc]==4:
                break
            abnomalEffectBoard[nr][nc]=time
            time+=v
            r,c = nr,nc
    # print(abnomalEffectBoard)

    #이제 탐색시작, 시작은 벽시간부터
    visited = [[0]*N for _ in range(N)]
    visited[floorStartR][floorStartC] =1
    q = deque()
    q.append((floorStartR,floorStartC,timeWallDuration+1))
    while q:
        r,c, time = q.popleft()
        if floorBoard[r][c]==4:
            return time

        for dr, dc in dList:
            nr, nc = r+dr, c+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            if visited[nr][nc]==0 and (floorBoard[nr][nc]==0 or floorBoard[nr][nc]==4) and (abnomalEffectBoard[nr][nc]==-1 or (-1<time+1<abnomalEffectBoard[nr][nc])):
                visited[nr][nc]=1
                q.append((nr,nc,time+1))
    return -1


#---!!!구동-----
#입력부 
N,M,F = map(int,input().split())
#미지공간
floorBoard = [list(map(int,input().split())) for _ in range(N)]
#동,서,남,북,윗면 순서
cubeBoardTri = [[list(map(int,input().split())) for _ in range(M)] for _ in range(5)]
#동,북,서,남,윗면 순으로 바꿔주기- 안해줘도 가능했었다.
cubeBoardTri[1],cubeBoardTri[3],cubeBoardTri[2] = cubeBoardTri[3],cubeBoardTri[2], cubeBoardTri[1]
abnomalEffect = [tuple(map(int,input().split())) for _ in range(F)]
abnomalEffectAlive = [1]*F
# 1. 시간의 벽에 탈출구 기록, 바닥탈출구 받기
floorStartR, floorStartC = setTimeWallExit()
# 2. 시간의 벽에서 3차원 BFS 진행
timeWallDuration = findTimeWallExit()
# 3. 미지공간에서 이상현상 고려하며
# 2차원 BFS 진행
unknownSpaceDuration = findUnSpaceExit(timeWallDuration, floorStartR,floorStartC)
#마지막 출력
if unknownSpaceDuration==-1:
    print(-1)
else:
    print(unknownSpaceDuration)
