N,M,B = map(int, input().split())

marr=[list(map(int, input().split())) for _ in range(N)]



# 1. 맵에서 블록 제거해서 인벤토리에 넣기  - 2초
# 2. 인벤토리에서 블록 꺼내서 맵에 놓기  - 1초


# 각각 좌표 지나가면서 - 


# 가장 높은 좌표 계산

max_floor = 0
for i in range(N):
    for j in range(M):
        max_floor=max(max_floor,marr[i][j])

# print(max_floor)

# - 1 가장 작은 부분 게산

min_floor = 1e9
for i in range(N):
    for j in range(M):
        min_floor=min(min_floor,marr[i][j])
# print(min_floor)

# 최소층- 최대층 해서 모두 맞추기

min_cost = 1e9
min_floor_set = min_floor-1
for floor in range(min_floor, max_floor+1):
    cost = 0
    tmp_inv = B
    
    for i in range(N):
        for j in range(M):
            # 블록 제거의경우
            if marr[i][j]> floor:
                sub_floor = marr[i][j]-floor
                tmp_inv+= sub_floor
                cost += sub_floor*2
            # 블록 쌓기의 경우
            else:
                sub_floor = floor - marr[i][j]
                tmp_inv -= sub_floor
                cost +=sub_floor
    if tmp_inv>=0 and cost<=min_cost:
        min_cost = cost
        min_floor_set = floor


print(min_cost, min_floor_set)
