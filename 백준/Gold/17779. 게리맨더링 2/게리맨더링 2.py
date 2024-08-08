#17779
N = int(input())
marr = [[0]*(N+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]

all_sum = sum(sum(i) for i in marr)

#(x,y)에서 가능한 d1, d2 경우의 수
def poss_d(x,y):
    poss_d = []
    for i in range(1,N):
        for j in range(1,N):
            if 1<=x<x+i+j<=N and 1<=y-i<y<y+j<=N:
                poss_d.append((i,j))
    return poss_d

#(x,y)에서 가능한 possd 뽑기
all_result = 1e9
def sub(x,y):
    global all_result
    now_possd = poss_d(x,y)
    for i in range(len(now_possd)):
        d1,d2 = now_possd[i]
        # print("now x, y, d1, d2:",x,y, d1,d2)
        #뽑았으면 진행

        five_map = [[0]*(N+1) for _ in range(N+1)]
        # 5번구역 만들기
        tmpx,tmpy = x,y
        for i in range(d1+1):
            five_map[tmpx+i][tmpy-i]=5
            five_map[tmpx+d2+i][tmpy+d2-i]=5
        for i in range(d2+1):
            five_map[tmpx+i][tmpy+i]=5
            five_map[tmpx+d1+i][tmpy-d1+i]=5

        # print("5번구역:")
        # print(*five_map, sep='\n')
        # print()
        popula = []
        #1번 선거구
        one = 0
        for r in range(1,x+d1):
            for c in range(1,y+1):
                if five_map[r][c]==5:
                    break
                one+=marr[r][c]
        popula.append(one)
        if one==0:
            break

        #2번 선거구
        two = 0
        for r in range(1,x+d2+1):
            for c in range(N,y,-1):
                if five_map[r][c]==5:
                    break
                two+=marr[r][c]
        popula.append(two)
        if two==0:
            break
        #3번 선거구
        three = 0
        for r in range(x+d1,N+1):
            for c in range(1,y-d1+d2):
                if five_map[r][c]==5:
                    break
                # print(r,c)
                three+=marr[r][c]
        popula.append(three)
        if three==0:
            break
        #4번 선거구
        four = 0
        for r in range(x+d2+1,N+1):
            for c in range(N,y-d1+d2-1,-1):
                if five_map[r][c]==5:
                    break
                four+=marr[r][c]
        popula.append(four)
        if four == 0:
            break
        #5번 선거구
        five = all_sum-sum(popula)
        if five==0:
            break
        popula.append(five)
        # print(popula)
        popula.sort()
        nowresult = popula[-1]-popula[0]
        all_result = min(all_result, nowresult)

#진행
for i in range(1,N+1):
    for j in range(1,N+1):
        sub(i,j)

print(all_result)