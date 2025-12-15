N = int(input())
marr = [list(map(int,input().split()))for _ in range(N)]
now_r, now_c =N//2, N//2
blowmap = [[[0,0,2,0,0],
           [0,10,7,1,0],
           [5,0,0,0,0],
           [0,10,7,1,0],
           [0,0,2,0,0]],
           [[0,0,0,0,0],
            [0,1,0,1,0],
            [2,7,0,7,2],
            [0,10,0,10,0],
            [0,0,5,0,0]],
            [[0,0,2,0,0],
             [0,1,7,10,0],
             [0,0,0,0,5],
             [0,1,7,10,0],
             [0,0,2,0,0]],
             [[0,0,5,0,0],
              [0,10,0,10,0],
              [2,7,0,7,2],
              [0,1,0,1,0],
              [0,0,0,0,0]]]
out= 0
d = [(-1,0),(0,1), (1,0), (0,-1)]
num =1
length, di,lencount = 1,0,0
while True:
    if (now_c, now_r) == (0,0):
        break
    
    #좌 하 우 상 순서
    dx, dy = d[di]
    if lencount ==2:
        lencount = 0
        length+=1

    for i in range(length):
        # print("토네이도 시작위치", now_r,now_c)
        # print("ccc")
        now_c+=dx
        now_r+=dy
        # # 모래 흩뿌려야할좌표 = now_r, now_c
        # # 토네이도 이동완료, 모레확산진행!!____-----
        # marr[now_r][now_c]=num
        # num+=1
        sum_blowed=0
        sum_outed=0
        sum_total=0
        sand = marr[now_r][now_c]
        marr[now_r][now_c]=0
        # print("뿌릴 모래:", sand)
        for r in range(5):
            for c in range(5):
                # 이동해야할 모레 좌표
                
                # 0,0 -> -2,2부터 진행
                # 뿌려야할 양(r,c) 뿌려야할 위치 (now_r+r-2,now_c+c-2)
                make_blow = (sand*blowmap[di][r][c])//100
                dest_r, dest_c = now_r+r-2, now_c+c-2
                if (0<=dest_r<N and 0<=dest_c<N):
                    #맵 안이므로 맵에 뿌리고 뿌린값에 저장
                    
                    marr[dest_r][dest_c]+=make_blow
                    sum_blowed+=make_blow
                else:
                    # 맵 밖이므로 나간곳에 저장
                    sum_outed+=make_blow
                sum_total+=make_blow
        alpha_r, alpha_c = now_r+dy, now_c+dx
        alpha = sand-sum_total
        if not(0<=alpha_r<N and 0<=alpha_c<N):
            sum_outed+=alpha
        else:
            marr[alpha_r][alpha_c]+=alpha
        out += sum_outed
        # print(marr)
        if (now_c, now_r) == (0,0):
            break
    
    lencount +=1

    di = (di+1)%4
# print(marr)
print(out)
