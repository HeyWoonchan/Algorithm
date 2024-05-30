from collections import deque
M,N = map(int, input().split())

marr = [list(map(int, input().split())) for _ in range(N)]

zerocnt = sum(1 if marr[i][j] == 0 else 0 for i in range(N) for j in range(M))
d = [(1,0),(0,1),(-1,0),(0,-1)]

total_trans = 0

q = deque([])
for y in range(N):
    for x in range(M):
        if marr[y][x] == 1:
            q.append((x,y,0))
        
max_day = 0

while q:
    x,y,day = q.popleft()
    if day>0:
        total_trans+=1
    max_day=max(max_day, day)

    for i in range(4):
        dx, dy = d[i]
        nx,ny = x+dx, y+dy
        if (0<=nx<M and 0<=ny<N) and marr[ny][nx]==0:
            marr[ny][nx]=1
            q.append((nx,ny,day+1))
    
if total_trans == zerocnt:
    print(max_day)
else:
    print(-1)