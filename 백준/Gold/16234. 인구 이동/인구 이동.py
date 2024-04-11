from collections import deque
import sys
sys.setrecursionlimit(10**5)
N,L,R = map(int, input().split())
marr = [list(map(int, input().split()))for _ in range(N)]

# visited = [[0 for _ in range(N)]for _ in range(N)]

# 영역전개
d = [(-1,0),(1,0),(0,-1),(0,1)]
used_cords=[]
def dfs(r,c):
    global used_cords
    # print("영역전개시작:",r,c)
    count = 0
    total_sum=0
    count+=1
    total_sum+= marr[r][c]
    visited[r][c]=1
    new_visited[r][c]=1
    locktb[r][c]=1
    used_cords.append((r,c))
    for i in range(4):
        dr,dc = d[i]
        nr,nc = r+dr, c+dc
        if not (0<=nr<N and 0<=nc<N):
            continue
        if visited[nr][nc]==0 and L<=abs(marr[r][c]-marr[nr][nc])<=R:
            # print("다음장소: ",nr,nc)
            # print(marr[r][c], marr[nr][nc], abs(marr[r][c]-marr[nr][nc]))
            visited[nr][nc]=1
            new_visited[nr][nc]=1
            locktb[nr][nc]=1
            rtotal_sum,rcount = dfs(nr,nc)
            count+=rcount
            total_sum+=rtotal_sum
    return total_sum,count

def bfs(r,c):
    queue = deque([(r,c)])
    visited[r][c]=1
    new_visited[r][c]=1
    sum =0
    total_count=0
    used_cords=[(r,c)]
    while queue:
        now_r, now_c= queue.popleft()
        total_count +=1
        sum+=marr[now_r][now_c]
        # print("영역전개시작:",now_r,now_c)
        for i in range(4):
            dr,dc = d[i]
            nr,nc = now_r+dr, now_c+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            if visited[nr][nc]==0 and L<=abs(marr[now_r][now_c]-marr[nr][nc])<=R:
                visited[nr][nc]=1
                new_visited[nr][nc]=1
                # print("다음장소: ",nr,nc)
                # print(marr[r][c], marr[nr][nc], abs(marr[now_r][now_c]-marr[nr][nc])
                queue.append((nr,nc))
                used_cords.append((nr,nc))
    area_people = sum//total_count
    for cords in used_cords:
        rr,cc = cords
        new_marr[rr][cc]=area_people
        locktb[rr][cc]=0

    return sum, total_count
    
    

new_marr=[[0 for _ in range(N)]for _ in range(N)]
new_visited =[[0 for _ in range(N)]for _ in range(N)]
locktb = [[0 for _ in range(N)]for _ in range(N)]
day=0
while True:
    # print(day,"번째날")
    #시작시 visited배열 초기화
    visited = [[0 for _ in range(N)]for _ in range(N)]
    continue_flag = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]==0:
                # print(r,c, "확인!")
                # visited[r][c]=1
                #new_visited 초기화
                # new_visited=[[0 for _ in range(N)]for _ in range(N)]
                #영역 찾기
                used_cords=[]
                area_sum ,area_count=dfs(r,c)
                area_people = area_sum//area_count
                for cords in used_cords:
                    rr,cc = cords
                    new_marr[rr][cc]=area_people
                if area_count>1:
                    continue_flag=True
                # print("인원분배후:")
                # print(new_marr)
    #더이상 바꿀게 없는지 확인
    if continue_flag==True:
        # print("바뀐적 있음! 다음날로")
        day+=1
    else:
        break

    #원래 맵에 다시 옮기기
    for r in range(N):
        for c in range(N):
            marr[r][c]=new_marr[r][c]

print(day)