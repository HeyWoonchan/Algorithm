R,C,T = map(int, input().split())
marr = [list(map(int, input().split()))for _ in range(R)]



d = [(1,0),(-1,0),(0,1),(0,-1)]
rotate_d= [[(0,1),(-1,0),(0,-1),(1,0)],
           [(0,1),(1,0),(0,-1),(-1,0)]
           ]

fresher=[]
dust_list = []
for r in range(R):
    for c in range(C):
        if marr[r][c]==-1:
            fresher.append((r,c))
        elif marr[r][c]!=0:
            dust_list.append((r,c))

def main():
    sec = 1
    while sec<=T:
        #확산과정
        new_marr = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if marr[r][c]==-1:
                    new_marr[r][c]=-1
                if marr[r][c]>0:
                    subdust = marr[r][c]//5
                    blowcnt = 0
                    for i in range(4):
                        dr,dc = d[i]
                        nr,nc = r+dr, c+dc
                        if not (0<=nr<R and 0<=nc<C):
                            continue
                        if marr[nr][nc]!=-1:
                            blowcnt+=1
                            new_marr[nr][nc]+=subdust
                    new_marr[r][c]+=marr[r][c] - subdust*blowcnt
        # print(new_marr)
        # print()
        # 회전과정
        # 청정기위쪽
        for i in range(2):
            fresher_r, fresher_c = fresher[i]
            direction = 0
            dr, dc = rotate_d[i][direction]
            start_r,start_c = fresher_r+dr, fresher_c+dc
            tmp=[0]*(R*C)
            j=1
            while True:
                if new_marr[start_r][start_c] == -1:
                    break
                tmp[j]=new_marr[start_r][start_c]
                new_marr[start_r][start_c]=tmp[j-1]
                if not (0<=start_r+dr<R and 0<=start_c+dc<C):
                    direction+=1
                dr, dc = rotate_d[i][direction]
                start_r,start_c=start_r+dr,start_c+dc
                j+=1
        # print(new_marr)
        #이동 다하면 new_marr->marr
        for r in range(R):
            for c in range(C):
                marr[r][c]=new_marr[r][c]

        sec+=1

    sum_dust = 0
    for r in range(R):
        for c in range(C):
            if new_marr[r][c]>0:
                sum_dust+=new_marr[r][c]

    print(sum_dust)

main()