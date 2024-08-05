#14499
N, M, r, c, K = map(int,input().split())
if M>1:
    marr = [list(map(int,input().split())) for _ in range(N)]
else:
    marr = [[int(input())] for _ in range(N)]
if K>1:
    commands = list(map(int,input().split()))
else:
    commands = [int(input())]

dice = [0]*7

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

for com in commands:
    if com==1:
        if c+1>=M:
            continue
        right()
        c+=1
    elif com==2:
        if c-1<0:
            continue
        left()
        c-=1
    elif com==3:
        if r-1<0:
            continue
        up()
        r-=1
    elif com==4:
        if r+1>=N:
            continue
        down()
        r+=1
    if marr[r][c]==0:
        marr[r][c]=dice[6]
    else:
        dice[6]=marr[r][c]
        marr[r][c]=0
    print(dice[1])