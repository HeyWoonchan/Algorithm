N,M,k = map(int, input().split())

marr= [list(map(int,input().split()))for _ in range(N)]

#1~4
nowdir_arr = list(map(int,input().split()))

#1~4
dir_priority=[[list(map(int, input().split())) for row in range(4)] for depth in range(M)]
# for _ in range(M):
#     dirs = []
#     for i in range(4):
#         dirs.append(list(map(int, input().split())))
#     dir_priority.append(dirs)
smellarr = []
for i in range(N):
    row = []
    for j in range(N):
        if marr[i][j]!=0:
            row.append([marr[i][j],k])
        else:
            row.append([0,0])
    smellarr.append(row)
# print(smellarr)


d = [(0,-1),(0,1),(-1,0),(1,0)]


def move_shark(x,y,shark_num,nowdir):
    mysmell_x, mysmell_y= -1,-1
    next_x, next_y = -1,-1
    mysmelldir = -1
    nextdir = -1
    for i in range(4):
        dx, dy = d[dir_priority[shark_num-1][nowdir][i]-1]
        nx, ny = x+dx, y+dy

        if not (0<=nx<N and 0<=ny<N): #벽 넘어가는지 확인
            # print("벽넘어가는방향!")
            continue
        if (mysmell_x,mysmell_y)==(-1,-1)and smellarr[ny][nx][0]==shark_num:
            mysmell_x, mysmell_y = (nx,ny)
            mysmelldir = dir_priority[shark_num-1][nowdir][i]
        elif smellarr[ny][nx][1]==0:
            next_x, next_y = nx,ny
            nextdir = dir_priority[shark_num-1][nowdir][i]
            break
    
    #lets move
    if (next_x,next_y)!= (-1,-1): #만약 이동할 곳이 있다면
        #원래자신냄새 -=1
        #냄새는 이동이 끝난 후 없애기
        if marr[next_y][next_x]==0: #상어가 없다면
            marr[y][x], marr[next_y][next_x] = 0, shark_num
        else:
            marr[y][x],marr[next_y][next_x] =0, min(marr[next_y][next_x], shark_num)
        smellarr[next_y][next_x] = [marr[next_y][next_x], 0]
        nowdir_arr[shark_num-1] = nextdir
        
    else: # 없으면 자신번호의 우선순위방향으로
        marr[y][x], marr[mysmell_y][mysmell_x] = 0, shark_num
        smellarr[mysmell_y][mysmell_x] = [marr[mysmell_y][mysmell_x], -1]
        nowdir_arr[shark_num-1] = mysmelldir
def test(arr):
    for i in range(len(arr)):
        print(arr[i])

# test(marr)
# test(smellarr)
# test(dir_priority)
step=1
while step<=1000:
    #상어 이동
    # print(step)
    visited = [0]*M
    # print(visited)
    for i in range(N):
        for j in range(N):
            # print(visited)
            if marr[i][j]!=0 and visited[marr[i][j]-1]==0:
                # print("상어 %d번 발견, %d 방문여부"%(marr[i][j],visited[marr[i][j]-1]))
                visited[marr[i][j]-1]=1
                move_shark(j,i,marr[i][j],nowdir_arr[marr[i][j]-1]-1)
                

    # print("이동완료")
    # test(marr)
    
    #냄새 수명 줄이기 (미리줄이기?)
    for i in range(N):
        for j in range(N):
            if smellarr[i][j][0]!=0:
                if smellarr[i][j][1]==0 or smellarr[i][j][1]==-1:
                    smellarr[i][j][1]=k
                    continue
                if smellarr[i][j][1]==1:
                    smellarr[i][j] = [0,0]
                
                else:
                    smellarr[i][j][1]-=1
    
    # test(smellarr)

    #상어가 몇마리인지 확인
    #2번이상 상어가 있는지 확인
    F = True
    for i in range(N):
        if F ==False:
            break
        for j in range(N):
            if marr[i][j]>=2:
                F = False
                break
    if F == True:
        break
    step+=1
if step <=1000:
    print(step)
else:
    print(-1)
