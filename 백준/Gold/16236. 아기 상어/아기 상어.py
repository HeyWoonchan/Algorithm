from collections import deque
N = int(input())
marr = [list(map(int,input().split())) for _ in range(N)]

nowcoord = (-1,-1)
for i in range(N):
    for j in range(N):
        if marr[i][j]==9:
            nowcoord=(i,j)
            marr[i][j]=0
            break
# print(nowcoord)
def bfs(nowshark, r,c):
    visited=[[0]*N for _ in range(N)]
    visited[r][c]=1

    d = [(-1,0),(0,-1),(0,1),(1,0)]
    q = deque([(r,c, 0)])

    minr = 1e9
    minc = 1e9
    mintime = 1e9
    while q:
        cur_r, cur_c, time = q.popleft()
        if 0<marr[cur_r][cur_c]<nowshark and time<=mintime:
            mintime=time
            if cur_r<minr:
                minr, minc = cur_r,cur_c
            elif cur_r==minr and cur_c<minc:
                minr, minc = cur_r,cur_c
            
        for dr,dc in d:
            nr,nc = cur_r+dr, cur_c+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            if visited[nr][nc]==0 and marr[nr][nc]<=nowshark:
                visited[nr][nc]=1
                q.append((nr,nc,time+1))
    return (minr,minc),mintime

nowShark = 2
nowTime = 0
eaten = 0

while True:
    nowcoord, time = bfs(nowShark,*nowcoord)
    # print(nowcoord,time,nowShark)
    if time==1e9:
        break
    i,j = nowcoord
    marr[i][j]=0
    eaten +=1
    nowTime+=time
    if eaten==nowShark:
        nowShark+=1
        eaten=0
    # print(*marr, sep='\n')
    # print()


print(nowTime)
