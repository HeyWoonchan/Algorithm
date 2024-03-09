# 청소년 상어

# 1 - up
# 2 - left up
# 3 - left
# 4 - left down
# 5 - down
# 6 - right down
# 7 - right
# 8 - right up

import copy
import sys

sys.setrecursionlimit(10**6)

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

direction = [[0 for _ in range(4)] for i in range(4)]
fish_num = [[0 for _ in range(4)] for i in range(4)]
visited = [[0] * 4 for i in range(4)]
for i in range(4):
    input_list = list(map(int, input().split()))
    for j in range(4):
        fish_num[i][j] = input_list[j * 2]
        direction[i][j] = input_list[j * 2 + 1]

result = 0


# 물고기 이동

def rotate(i, j,sx,sy, board, dirBoard):
    nnx = j + dx[dirBoard[i][j] - 1]
    nny = i + dy[dirBoard[i][j] - 1]
    way = dirBoard[i][j]
    tmp_way = dirBoard[i][j]
    # 지금 nx ny에는 상어가 있거나 물고기가 아예 없는 상태
    # 한바퀴를 돌때까지 해당 방향으로 못간다면 아예 그 번호는 스킵
    count = 1
    # print("checking way %d.."%way)
    while count <= 7:
        if nnx < 0 or nny < 0 or nnx > 3 or nny > 3:
            # print("now way %d can't move, way set to next"%way)
            nnx = j + dx[(dirBoard[i][j] - 1 + count) % 8]
            nny = i + dy[(dirBoard[i][j] - 1 + count) % 8]
            way = (dirBoard[i][j] + count) % 8
        elif nnx == sx and nny == sy:
            # print("now way %d can't move because of shark, way set to next"%way)
            nnx = j + dx[(dirBoard[i][j] - 1 + count) % 8]
            nny = i + dy[(dirBoard[i][j] - 1 + count) % 8]
            way = (dirBoard[i][j] + count) % 8
        else:
            # print("%d way satisfied"%way)
            break
        count += 1
    if count >= 8:
        way = tmp_way
    return nnx, nny, way


def move_fish(sx,sy,board, dirBoard):
    for k in range(1, 17):

        # print("moving fish %d.."%k)
        fish_flag = False
        for i in range(4):
            if fish_flag:
                continue
            for j in range(4):
                if fish_flag:
                    continue
                if board[i][j] == k:
                    nx, ny, way_r = rotate(i, j,sx,sy,board,dirBoard)
                    dirBoard[i][j] = way_r
                    if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                        continue
                    elif sx==nx and sy ==ny:
                        # 이동방향에 상어가 있으므로  다음
                        continue
                    board[i][j], board[ny][nx] = board[ny][nx], board[i][j]
                    dirBoard[i][j], dirBoard[ny][nx] = dirBoard[ny][nx], dirBoard[i][j]

                    # print("move %d way %d"%(k, way_r))
                    # for m in range(4):
                    #     for n in range(4):
                    #         print(fish_num[m][n], end=' ')
                    #     print()
                    # print()
                    fish_flag = True

# greedy approach -상어 진행 방향 중에서 가장 큰것만 먹기 - 해보니 안됨
# 각각을 recursive하게 진행하여 최대값을 찾아보자.


def sol(shark_x, shark_y, score, board, dirBoard):
    # 물고기 진행 후 상어가 갈수 있는 곳으로 상어 이동
    global result
    score += board[shark_y][shark_x]
    result = max(result, score)
    board[shark_y][shark_x] = 0

    move_fish(shark_x, shark_y, board, dirBoard)


    for i in range(1,5):
        shark_nx = shark_x+ dx[dirBoard[shark_y][shark_x]-1]*i
        shark_ny = shark_y+ dy[dirBoard[shark_y][shark_x]-1]*i
        if (0<= shark_nx <4 and 0<=shark_ny <4) and board[shark_ny][shark_nx]>0:
            sol(shark_nx,shark_ny,score, copy.deepcopy(board), copy.deepcopy(dirBoard))


sol(0,0,0,fish_num,direction)

print(result)