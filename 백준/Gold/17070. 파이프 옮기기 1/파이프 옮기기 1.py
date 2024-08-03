#17070

N = int(input())
marr = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
# state 0:가로, 1:세로, 2:대각선

def checknext(r,c, state):
    if not (0<=r<N and 0<=c<N):
        return False
    if state==0  and marr[r][c]==0:
        return True
    if state==1 and marr[r][c]==0:
        return True
    if state==2:
        flag = True
        for dr,dc in [(0,0),(0,-1),(-1,0)]:
            nr,nc = r+dr,c+dc
            if marr[nr][nc]==1:
                flag=False
                break
        return flag

def sol(r,c,state):
    global cnt,N

    if state == 0:
        for dr, dc, nextState in [(0,1,0),(1,1,2)]:
            nr,nc = r+dr, c+ dc
            #다음상태 체크
            if checknext(nr,nc,nextState):
                if (nr,nc)==(N-1,N-1):
                    cnt+=1
                else:
                    sol(nr,nc,nextState)
    elif state==1:
        for dr, dc, nextState in [(1,0,1),(1,1,2)]:
            nr,nc = r+dr, c+ dc
            #다음상태 체크
            if checknext(nr,nc,nextState):
                if (nr,nc)==(N-1,N-1):
                    cnt+=1
                else:
                    sol(nr,nc,nextState)
    else:
        for dr, dc, nextState in [(0,1,0),(1,0,1),(1,1,2)]:
            nr,nc = r+dr, c+ dc
            #다음상태 체크
            if checknext(nr,nc,nextState):
                if (nr,nc)==(N-1,N-1):
                    cnt+=1
                else:
                    sol(nr,nc,nextState)


if marr[N-1][N-1]==1:
    print(0)
else:
    sol(0,1,0)
    print(cnt)