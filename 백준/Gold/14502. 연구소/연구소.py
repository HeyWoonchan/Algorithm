import sys

n, m = map(int, input().split())
sys.setrecursionlimit(10**6)

virusMap = [[0 for j in range(m)] for i in range(n)]
originMap = [[0 for j in range(m)] for i in range(n)]


for i in range(n):
    virusMap[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        originMap[i][j]=virusMap[i][j]
# for i in range(n):
#     for j in range(m):
#         print(virusMap[i][j], end=" ")
#     print()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    """
    상하좌우 방문

    만약 벽에 부딪히거나 맵 밖을 넘어가면 방문 중지

    해당 자리가 0 이면 미방문이라는 뜻임
    안부딛히면 그냥 그자리에서 또 진행하는데
    방문기록 남겨서 안방문한곳만 진행
    진행완료인 곳은 2로 변경

    :param i:
    :param j:
    :return:
    """


    if virusMap[x][y] == 0:
        virusMap[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if virusMap[nx][ny] == 0:
                virusMap[nx][ny]=2
                dfs(nx, ny)




max = 0

for i in range(n*m):
    for j in range(i+1, n*m):
        for k in range(j+1, n*m):
            x_list = [i//m, j//m,k//m]
            y_list = [i%m, j%m, k%m]

            err_flag = False
            for l in range(3):
                if originMap[x_list[l]][y_list[l]] != 0:
                    err_flag = True
                    break

            if err_flag:
                continue
            # print("첫번째 좌표= ", i//m, i%m)
            for l in range(3):
                originMap[x_list[l]][y_list[l]] = 1
            for p in range(n):
                for q in range(m):
                    virusMap[p][q] = originMap[p][q]

            # print("세팅완료된  map")
            # for i in range(n):
            #     for j in range(m):
            #         print(virusMap[i][j], end=" ")
            #     print()
            # print()

            for p in range(n):
                for q in range(m):
                    if originMap[p][q] == 2:
                        dfs(p, q)
            count = 0
            for p in range(n):
                for q in range(m):
                    if virusMap[p][q] == 0:
                        count+=1
            # if count>2:
            #     print("감염이후 map")
            #     for p in range(n):
            #         for q in range(m):
            #             print(virusMap[p][q], end=" ")
            #         print()
            #     print("0 카운트 : ", count)
            #     print()

            if max<count:
                max = count
            for l in range(3):
                originMap[x_list[l]][y_list[l]] = 0

            # print("원래대로 돌아간 map")
            # for i in range(n):
            #     for j in range(m):
            #         print(originMap[i][j], end=" ")
            #     print()
            # print()
            # print()


print(max)
