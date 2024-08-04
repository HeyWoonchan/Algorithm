#21609

#기준 블록: 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록,
# 그러한 블록이 여러개면 얼의 번호가 가장 작은 블록
# 
# 1.크기가 가장 큰 블록 그룹 찾기(무지개 블록의 수가 가장 많은 블록, 여러개라면 기준 블록의 행이 가장 큰것, 여러개라면 열이 가장 큰것)
#
# 2. 블록 그룹의 모든 블록 제거, 제거 개수^2점 획득
# 
# 3. 격자에 중력 작용
# 4. 격자 반시계 회전
# 5. 다시 중력 작용

# 1~5 반복 ( 블록그룹 존재하는 동안 )

from collections import deque

# input
N, M = map(int, input().split())
if N==1:
    marr=[int(input())]
else:
    marr = [list(map(int,input().split())) for _ in range(N)]

# 블록그룹찾기 0<블록숫자<=M 부터 시작
visited = [[0]*N for _ in range(N)] #맵 한번돌때 한번만필요
def bfs(r,c,startColor):
    visited[r][c]=1
    q = deque([(r,c)])
    d = [(1,0),(0,1),(-1,0),(0,-1)]

    base_r,base_c = 500,500
    cnt= 0
    mujicount=0
    results = []
    while q:
        now_r, now_c = q.popleft()
        if marr[now_r][now_c]!=0:
            results.append((now_r,now_c))
        else:
            mujicount+=1
        cnt +=1
        for dr,dc in d:
            nr,nc = now_r+dr, now_c+dc

            if not (0<=nr<N and 0<=nc<N):
                continue
            if visited[nr][nc]==0 and (marr[nr][nc]==startColor or marr[nr][nc]==0):
                visited[nr][nc]=1
                q.append((nr,nc))
    results.sort(key=lambda x:(x[0],x[1]))
    base_r,base_c=results[0]
    return base_r,base_c,cnt,mujicount

#블록그룹지우기+점수계산
def bfs_del(r,c,startColor):
    visited = [[0]*N for _ in range(N)]
    visited[r][c]=1
    q = deque([(r,c)])
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    score=0
    while q:
        now_r, now_c = q.popleft()
        marr[now_r][now_c]=-2
        score+=1
        for dr,dc in d:
            nr,nc = now_r+dr, now_c+dc

            if not (0<=nr<N and 0<=nc<N):
                continue
            if visited[nr][nc]==0 and (marr[nr][nc]==startColor or marr[nr][nc]==0):
                visited[nr][nc]=1
                q.append((nr,nc))
    return score

#중력작용하기
def gravity():
    for j in range(N):
        i = 0

        #내릴 시작점 찾기
        start = 0
        while i<N-1:
            if marr[i][j]==-1 or 0<=marr[i][j]<=M:
                start = i
            i+=1
                 
        # print("down start:",i,j)
        #시작점 찾았으면 내리기
        if start == N:
            continue
        for k in range(start,-1,-1):
            if marr[k][j]==-1:
                continue
            l = k
            while l<N-1:
                if marr[l+1][j]==-2:
                    marr[l][j],marr[l+1][j]=marr[l+1][j],marr[l][j]
                    l+=1
                else:
                    break

#반복시작

if N==1:
    print(0)
    
else:
    totalScore=0
    while True:

        #1. 가장큰 블록그룹찾기 
        visited = [[0]*N for _ in range(N)]
        
        results=[]
        for i in range(N):
            for j in range(N):
                if visited[i][j]==0 and 0<marr[i][j]<=M:
                    base_r,base_c, cnt,mujicnt = bfs(i,j,marr[i][j])
                    
                    for k in range(N):
                        for l in range(N):
                            if marr[k][l]==0:
                                visited[k][l]=0
                    if cnt>=2:
                        results.append((base_r,base_c,cnt,mujicnt))
        
        #찾은 블록이 없다면 끝내기
        if len(results)==0:
            break

        # print(maxbase_r,maxbase_c,maxcnt)
        #2. 블록그룹지우기(빈칸: -2)
        results.sort(key=lambda x:(x[2],x[3],x[0],x[1]))
        maxbase_r,maxbase_c,maxcnt, maxmujicnt = results[-1]
        score = bfs_del(maxbase_r,maxbase_c, marr[maxbase_r][maxbase_c])
        # print(score**2)
        totalScore+=score**2
        # print(*marr, sep='\n')
        # print()
        #3. 중력작용하기
        gravity()
        # print(*marr, sep='\n')
        # print()
        #4. 반시계 회전
        
        marr= list(map(list,zip(*[marr[i][::-1] for i in range(N)])))
        # print(*marr, sep='\n')
        # print()
        #5. 중력
        gravity()
        # print(*marr, sep='\n')
        # print()
        # print('회차끝')

    print(totalScore)
        