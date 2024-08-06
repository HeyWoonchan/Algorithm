from collections import deque

dice = [0,1,2,3,4,5,6]

def left():
    dice[4],dice[1],dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]

def right():
    dice[4],dice[1],dice[3], dice[6] = dice[6],dice[4],dice[1], dice[3]

def up():
    dice[2],dice[6] = dice[6], dice[2]
    dice[1], dice[5] = dice[5], dice[1]
    dice[2],dice[5] = dice[5], dice[2]

def down():
    dice[2],dice[6] = dice[6], dice[2]
    dice[1], dice[5] = dice[5], dice[1]
    dice[1],dice[6] = dice[6], dice[1]


def bfs(r,c):
    visited = [[0]*M for _ in range(N)]
    visited[r][c]=1
    q = deque([(r,c)])
    d = [(1,0),(-1,0),(0,1),(0,-1)]

    cnt = 0
    while q:
        now_r, now_c = q.popleft()

        cnt+=1
        for dr, dc in d:
            nr, nc = now_r+dr, now_c+dc

            if not (0<=nr<N and 0<=nc<M):
                continue
            if visited[nr][nc]==0 and marr[nr][nc] == marr[now_r][now_c]:
                visited[nr][nc] = 1
                q.append((nr,nc))
    return cnt


N, M, K = map(int, input().split())
marr = [list(map(int,input().split())) for _  in range(N)]
x,y= 0,0
dir = 0
# 동:0 남:1 서:2 북:3

totalScore= 0
for _ in range(K):
    if dir == 0:
        if y+1>=M:
            dir = (dir+2)%4
            y-=1
            left()
        else:
            y+=1
            right()
    elif dir ==1:
        if x+1>=N:
            dir = (dir+2)%4
            x-=1
            up()
        else:    
            x+=1
            down()
    elif dir==2:
        if y-1<0:
            dir = (dir+2)%4
            y+=1
            right()
        else:
            y-=1
            left()
    else:
        if x-1<0:
            dir = (dir+2)%4
            x+=1
            down()
        else:
            x-=1
            up()

    score = bfs(x,y)
    totalScore+=score*marr[x][y]
    if dice[6]>marr[x][y]:
        dir= (dir+1)%4
    elif dice[6]<marr[x][y]:
        dir= (dir-1)%4
    

print(totalScore)