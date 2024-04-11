# 치킨 배달

"""
맵 받고

bfs 돌리면 최소거리치킨집 계산가능, 골라진 치킨집의 거리는 문제 공식으로 계산

가장 많이 수익내는 치킨집은 최대 M개이다
0~M개 고르고, 나머지 치킨집 모두 폐업

->>도시의 치킨거리가 가장 작게 0~M개를 냅두고, 나머지는 없애기

치킨집 1개선택, ~~치킨집 M개 선택

각각 선택 수 별로 치킨거리 계산



---------------

input

치킨집 골라놓기

decision space

1치킨집폐업/유지  -> 2치킨집 폐업/유지 -> ... -> N번 치킨집 폐업/유지

-> 폐업/유지 배열에 유지되는 치킨집 M개 이하일때만 고려

해당 맵별로 치킨거리 계산(bfs)


"""


#input
from collections import deque
N, M = map(int, input().split())

city = [list(map(int, input().split()))for _ in range(N)]
#0:빈칸, 1:집, 2:치킨집

#치킨집 골라놓기
bhc_list = [] #r,c
house_list = []
for r in range(N):
    for c in range(N):
        if city[r][c]==2:
            bhc_list.append((r,c))
            city[r][c]=0 #치킨집 다시세팅 위해서 0으로 설정
        if city[r][c]==1:
            house_list.append((r,c))

#집도 미리 저장해두기


# print(city)
#치킨집 거리계산함수
# def bfs_bhc_dist(r,c):
#     visited_bfs = [[0 for _ in range(N)] for _ in range(N)]
#     visited_bfs[r][c]=1
#     queue = deque([(r,c)])
#     d = [(1,0),(-1,0),(0,1),(0,-1)]
#     while queue:
#         now_r, now_c = queue.popleft()
#         # 치킨집이면 리턴
#         if city[now_r][now_c]==2:
#             return now_r,now_c

#         for i in range(4):
#             dr, dc= d[i]
#             nr, nc = now_r+dr, now_c+dc
#             if not (0<=nr<N and 0<=nc<N):
#                 continue
#             if visited_bfs[nr][nc]==0:
#                 # print(nr,nc,"로 진행")
#                 visited_bfs[nr][nc]=1
#                 queue.append((nr,nc))
#     # print("치킨집없음!")
#     return (r,c) #갈 수 있는 치킨집이 없는 경우



# print(bhc_list)
visited = [0] * len(bhc_list)

total_dist = 1e9


def pick_bhc(depth, set_bhc,c):
    global total_dist
    if depth == len(bhc_list) and len(set_bhc)<=M:
        if len(set_bhc)>0:
            #치킨집 다시세팅
            # print(set_bhc)
            for bhc in set_bhc:
                city[bhc[0]][bhc[1]]=2
            # print(city)
            #각 집 거리계산
            sum_dist=0
            for house in house_list:
                # print("현재집:",y,x)
                y,x = house
                # bhc_y, bhc_x = bfs_bhc_dist(y,x)
                # # print("가까운 치킨집 :",bhc_y, bhc_x)
                # # print()
                bhc_dist= 99999
                #제일 가까운 치킨집 거리
                for bhc in set_bhc:
                    bhc_y, bhc_x = bhc
                    bhc_dist =min(bhc_dist,abs(y-bhc_y)+abs(x-bhc_x))
                sum_dist+=bhc_dist
            total_dist = min(total_dist, sum_dist)
            for bhc in set_bhc:
                city[bhc[0]][bhc[1]]=0
        return
    for i in range(c,len(bhc_list)):
        if visited[i]==0:
            visited[i]=1
            pick_bhc(depth+1, set_bhc+[bhc_list[i]],i+1) #고르는경우
            pick_bhc(depth+1,set_bhc,i+1) #안고르는경우
        visited[i]=0
pick_bhc(0,[],0)
print(total_dist)