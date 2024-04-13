from collections import deque

N = int(input())
K = int(input())

apple_list= [list(map(int,input().split())) for _ in range(K)]

L = int(input())

command_list = []

for _ in range(L):
    a,b = input().split()
    command_list.append((int(a),b))


# 상 우 하 좌
d = [(-1,0),(0,1),(1,0),(0,-1)]

snake = deque([(0,0)])


marr= [[0]*N for _ in range(N)]
marr[0][0]=1

for apple in apple_list:
    r,c = apple
    marr[r-1][c-1]=2
def main():
    time=0
    now_d = 1
    for command in command_list:
        t, com = command
        while time<t:
            time+=1
            # print("now time:",time)
            r,c = snake[-1]
            # print("now snake head = ",r,c)
            dr,dc= d[now_d]
            nr,nc = r+dr, c+dc
            if not (0<=nr<N and 0<=nc<N): # 맵밖 -> 게임끝
                print(time)
                return
            if marr[nr][nc]==1: # 자신의 몸 -> 게임끝
                print(time)
                return
            elif marr[nr][nc]==2: #사과
                snake.append((nr,nc))
                marr[nr][nc]=1
            else: # 빈 길
                tail_r, tail_c = snake.popleft()
                marr[tail_r][tail_c]=0
                marr[nr][nc]=1
                snake.append((nr,nc))
            # print(snake)
            # for i in range(len(marr)):
            #     print(marr[i])
            # print(time, "초 이동끝\n")
        # print(time,"초, 방향변경")
        if com=='L':
            now_d = (now_d-1)%4
        else:
            now_d = (now_d+1)%4

    # print("command 종료, 계속이동시작")
    
    while True:
        time+=1
        # prin/t("now time:",time)
        r,c = snake[-1]
        # print("now snake head = ",r,c)
        dr,dc= d[now_d]
        nr,nc = r+dr, c+dc
        if not (0<=nr<N and 0<=nc<N): # 맵밖 -> 게임끝
            print(time)
            return
        if marr[nr][nc]==1: # 자신의 몸 -> 게임끝
            print(time)
            return
        elif marr[nr][nc]==2: #사과
            snake.append((nr,nc))
            marr[nr][nc]=1
        else: # 빈 길
            tail_r, tail_c = snake.popleft()
            marr[tail_r][tail_c]=0
            marr[nr][nc]=1
            snake.append((nr,nc))
        # print(snake)
        # for i in range(len(marr)):
        #     print(marr[i])
        

main()