#21610

N, M = map(int,input().split())
marr = [list(map(int,input().split())) for _ in range(N)]

movement = [tuple(map(int,input().split())) for _ in range(M)]


#비바라기 시전
cloudmap = [[0]*N for _ in range(N)]
cloudmap[N-1][0]=1
cloudmap[N-1][1]=1
cloudmap[N-2][0]=1
cloudmap[N-2][1]=1

directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

#구름 이동
def move(direction, dist):
    dr, dc = directions[direction-1]
    newcloudmap = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cloudmap[i][j]==1:
                nr,nc = (i+dr*dist)%N, (j+dc*dist)%N
                newcloudmap[nr][nc]=1
    return newcloudmap

#구름칸 물양증가+구름삭제+ 물복사버그
def rain():
    #물양증가
    for i in range(N):
        for j in range(N):
            if cloudmap[i][j]==1:
                marr[i][j]+=1
    #물복사버그+ 구름삭제
    check_d = [(-1,-1),(-1,1),(1,-1),(1,1)]
    for i in range(N):
        for j in range(N):
            if cloudmap[i][j]==1:
                cnt = 0
                for dr,dc in check_d:
                    nr,nc = i+dr, j+dc
                    if not (0<=nr<N and 0<=nc<N):
                        continue
                    if marr[nr][nc]>0:
                        cnt+=1
                marr[i][j]+=cnt
    
    #구름생기고 물줄어들기(위에서 구름 사라지는게 아닐경우)
    for i in range(N):
        for j in range(N):
            if cloudmap[i][j]==1:
                cloudmap[i][j]=0
                continue
            if marr[i][j]>=2:
                cloudmap[i][j]=1
                marr[i][j]-=2

for d, s in movement:
    cloudmap = move(d,s)
    rain()
print(sum(sum(marr[i]) for i in range(N)))