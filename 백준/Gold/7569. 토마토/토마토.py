from collections import deque
M,N,H = map(int, input().split())
marr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
d = [(0,0,1),(0,1,0),(1,0,0),(-1,0,0),(0,-1,0),(0,0,-1)]

#안익은토마토 시작개수
starttomatoes=0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if marr[h][n][m]==0:
                starttomatoes+=1

#bfs
def bfs():
    #모든 시작 토마토 큐에 넣기
    worktomatoes=0
    totaldays=0
    q = deque([])
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if marr[h][n][m]==1:
                    q.append((m,n,h,0))

    while q:
        m,n,h,days = q.popleft()
        
        totaldays = max(totaldays,days)
        for i in range(6):
            dm,dn,dh = d[i]
            nm,nn,nh= m+dm, n+dn, h+dh
            if not (0<=nm<M and 0<=nn<N and 0<=nh<H):
                continue
            if marr[nh][nn][nm]==0:
                q.append((nm,nn,nh,days+1))
                worktomatoes+=1
                marr[nh][nn][nm]=1
    return worktomatoes, totaldays

worktomatoes, totaldays = bfs()
# print(starttomatoes, worktomatoes)
#모든 토마토가 익었는가?
if worktomatoes==starttomatoes:
    print(totaldays)
else:
    print(-1)


