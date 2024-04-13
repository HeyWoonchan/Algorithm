N,M,K = map(int, input().split())


foodmap_update = [list(map(int,input().split())) for _ in range(N)]

# print(foodmap_update)

tree_info = [list(map(int, input().split()))for _ in range(M)]
foodmap = [[5] *N for _ in range(N)]

# print(foodmap)
marr = [[[]for _ in range(N)] for _ in range(N)]
# print(marr)

d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


def main():
    for tree in tree_info:
        r,c,age = tree
        marr[r-1][c-1].append(age)
    live = M
    for year in range(K):
        # print(year,"년 시작")
        #봄
        die_info = []
        for r in range(N):
            for c in range(N):
                if len(marr[r][c])!=0:
                    marr[r][c].sort()
                    die_idx = len(marr[r][c])
                    for i in range(len(marr[r][c])):
                        #나이만큼 양분 먹기
                        if foodmap[r][c]-marr[r][c][i]<0:
                            # print(r,c,i ,": 먹이부족, 사망! 나이:",marr[r][c][i] )
                            #죽는거면 양분으로 추가
                            # foodmap[r][c]+=marr[r][c][i]//2
                            die_info.append((r,c,marr[r][c][i]))
                            live-=1
                            die_idx = min(die_idx,i)
                        else:
                            # print(r,c, "나무존재, 먹이 먹을수 있음, 나이업")
                            foodmap[r][c]-=marr[r][c][i]
                            marr[r][c][i]+=1
                    marr[r][c]=marr[r][c][:die_idx]
        
        #여름
        for die in die_info:
            r,c,z = die
            foodmap[r][c]+=z//2
                    
        # for i in range(len(marr)):
        #     print(marr[i])
        
        #가을 번식
        # print("번식시작")
        for r in range(N):
            for c in range(N):
                if len(marr[r][c])!=0:
                    for i in range(len(marr[r][c])):
                        if marr[r][c][i]%5==0:
                            for j in range(8):
                                dr,dc = d[j]
                                nr,nc = r+dr, c+dc
                                if not (0<=nr<N and 0<=nc<N):
                                    continue
                                marr[nr][nc].append(1)
                                live+=1
        # for i in range(len(marr)):
        #     print(marr[i])
        # print("번식끝")
        #겨울 양분추가

        for r in range(N):
            for c in range(N):
                foodmap[r][c]+=foodmap_update[r][c]


    print(live)

main()
