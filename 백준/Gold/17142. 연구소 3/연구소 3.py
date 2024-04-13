from collections import deque
N,M = map(int,input().split())
marr= [list(map(int,input().split()))for _ in range(N)]


# 바이러스 정보 저장
virus_info =[]
wallcheck=0
for r in range(N):
    for c in range(N):
        if marr[r][c]==2:
            virus_info.append((r,c))
        if marr[r][c]==1:
            wallcheck+=1


# 바이러스 확산 함수(dfs-x bfs로 진행(동시진행해야함))

d = [(1,0),(-1,0),(0,1),(0,-1)]


def bfs(picked):
    global wallcheck
    queue=deque([]) # r,c,time 

    new_marr = [[-1 for _ in range(N)] for _ in range(N)]
    
    
    for r in range(N):
        for c in range(N):
            if marr[r][c]==2:
                flag = False
                for i in range(4):
                    dr,dc= d[i]
                    nr,nc= r+dr, c+dc
                    if not (0<=nr<N and 0<=nc<N):
                        continue
                    if marr[nr][nc] !=1:
                        flag= True
                if flag==False:
                    new_marr[r][c]=-3
    answer= 0

    # for j in range(N):
    #     print(new_marr[j])
    for coord in picked:
        r,c = coord
        queue.append((r,c))
        new_marr[r][c]=0
    while queue:
        #여기서 처리
        # print(queue)
        r,c= queue.popleft()
        # if new_marr[r][c]==-3 or new_marr[r][c]==-2:
        #     new_marr[r][c]=time #time
        # new_marr[r][c]=time
        # print("1")
        # print(new_marr)
        #여기서는 넣기만
        flag = False
        for i in range(4):
            dr,dc= d[i]
            nr,nc= r+dr, c+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            if new_marr[nr][nc] ==-1 and marr[nr][nc]==0:
                # print(nr,nc,"확산")
                queue.append((nr,nc))
                new_marr[nr][nc] = new_marr[r][c]+1
                answer = max(answer, new_marr[nr][nc])
                # print(new_marr)
                flag = True
            elif new_marr[nr][nc]==-1 and marr[nr][nc]==2: #다음것이 비활성 바이러스라면
                # new_marr[nr][nc]=time+1
                queue.append((nr,nc))
                new_marr[nr][nc]=new_marr[r][c]+1
                flag = True
                # print("비활성->활성")
                # print(new_marr)
                # for j in range(4):
                #     ddr, ddc = d[j]
                #     nnr = nr+ddr
                #     nnc = nc+ddc
                #     if not (0<=nnr<N and 0<=nnc<N):
                #         continue
                #     #긴급사항 먼저 넣어주기
                #     if new_marr[nr][nc]==-3:
                #         queue.appendleft((nnr,nnc,1)) #활성으로변경
        # if flag == False:
        #     new_marr[r][c]=0
    # for i in range(len(new_marr)):
    #     print(new_marr[i])
    # print()
    # print(new_marr)
    # print()
    time_spended=0
    # 닿지 못한 곳이 있는지 확인 + 걸린 초 확인
    check=0
    for r in range(N):
        for c in range(N):
            if new_marr[r][c]==-1:
                check+=1
    if check==wallcheck:
        return answer
    return 1e9
    




# 바이러스 뽑기
total_time = 1e9
def sol(depth, picked_virus,curr):
    global total_time
    if depth ==M:
        #M개 뽑기 완료, 확산 진행
        # print(picked_virus)
        result = bfs(picked_virus)
        total_time = min(total_time, result)


    for i in range(curr,len(virus_info)):
        sol(depth+1, picked_virus + [virus_info[i]],i+1)


sol(0,[],0)

if total_time == 1e9:
    print(-1)
else:
    print(total_time)