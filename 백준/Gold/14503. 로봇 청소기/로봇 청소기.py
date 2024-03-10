# 로봇 청소기

# 0 - north
# 1 - east
# 2 - south
# 3 - west

# output - 청소한 칸의 개수
import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(x, y, way,board):

    #print("%d,%d 위치, 진행시작"%(x,y))

    if board[x][y] == 0:
        board[x][y] = 2
        #print("현위치 %d, %d 청소완료"%(x,y))
        # for i in range(N):
        #     for j in range(M):
        #         print(board[i][j],end=' ')
        #     print()
    nr, nc = -1, -1
    for i in range(4):  # 주변에 청소할 공간이 있는지 확인
        nx = x + dr[i]
        ny = y + dc[i]
        if board[nx][ny] == 0:
            nr, nc = ny, nx
    if nr == -1 and nc == -1:  # 주변에 청소할 공간이 없다면 후진할 수 있는지 확인
        #print("4방향중 청소공간 x")
        br = x + dr[(way + 2) % 4]
        bc = y + dc[(way + 2) % 4]
        if board[br][bc] == 1:
            #print("후진불가, 작동종료")
            return
        else:
            #print("후진가능, 후진후 다시진행")
            dfs(br, bc, way,board)
    else:
        #print("청소공간 존재, 방향 45도 반시계 돌리고 해당방향 길 확인")
        nway = (way - 1) % 4
        nr = x + dr[nway]
        nc = y + dc[nway]

        if board[nr][nc] == 0:
            #print("돌린방향(%d,%d)에 청소안한부분 존재, 그부분으로 가서 다시진행"%(nr,nc))
            dfs(nr, nc, nway,board)
        else:
            #print("돌린방향(%d,%d)에 청소안한부분 없음, 현위치에서 방향만 바꾸고 다시진행"%(nr,nc))
            dfs(x, y, nway,board)
    return


dfs(r, c, d,room)

result = 0
for i in range(N):
    for j in range(M):
        if room[i][j]==2:
            result+=1

print(result)
