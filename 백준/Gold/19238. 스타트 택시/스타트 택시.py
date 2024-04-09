from collections import deque

N,M,fuel=map(int,input().split())
marr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
taxi_y, taxi_x = map(int, input().split())
passengers = [list(map(int, input().split()))for _ in range(M)]

d = [(-1,0),(1,0), (0,-1),(0,1)]
dist = 1e9
found = -1
# def distance(length, x,y, to_find):  
#     global found, dist
#     #거리찾는 함수
#     if length>dist:
#         return
#     if to_find==-1:
#         if marr[y][x]!= 0:
#             if dist == length:
#                 return
#             dist = min(dist, length)
#             if dist == length:
#                 found = marr[y][x]
#             return
#     else:
#         if marr[y][x]==to_find:
#             dist = min(dist, length)
#             if dist == length:
#                 found = marr[y][x]
#             return
#     for i in range(4):
#         dx, dy = d[i]
#         nx, ny= x+dx, y+dy
#         if not (0<=nx<N and 0<=ny<N):
#             continue
#         if visited[ny][nx] ==0 and marr[ny][nx] != 1:
#             visited[ny][nx]=1
#             distance(length+1, nx,ny, to_find)
#             visited[ny][nx]=0

def bfs(x,y,to_find): # bfs 로 찾은 경로는 항상 최단경로!!
    visited = [[0]*N for _ in range(N)]
    queue = deque([(x,y,0)])
    visited[y][x]=1

    found = []
    while queue:
        tx,ty,length = queue.popleft()
        if to_find==-1 and marr[ty][tx]!=0:
            found.append((tx,ty,length))
        if to_find!=-1 and marr[ty][tx]==to_find:
            return marr[ty][tx], length
        for i in range(4):
            dx, dy = d[i]
            nx, ny = tx+dx, ty+dy
            if not(0<=nx<N and 0<=ny<N):
                continue
            if visited[ny][nx]==0 and marr[ny][nx]!=1:
                visited[ny][nx]=1
                queue.append((nx,ny,length+1))
    if found:
        found.sort(key=lambda x:(x[2],x[1],x[0]))
        return marr[found[0][1]][found[0][0]], found[0][2]

    return marr[y][x], length
    
def test():
    for i in range(len(marr)):
        print(marr[i])

flag = True
completed = [0]*M
for step in range(M):
    # 택시위치로부터 손님찾기시작
    # 맵에 손님 세팅
    for i in range(len(passengers)):
        if completed[i]==1:
            continue
        y = passengers[i][0]
        x = passengers[i][1]
        marr[y-1][x-1]=i+2
    dist = 1e9
    found = -1
    # test()
    # distance(0,taxi_x-1,taxi_y-1,-1)
    found, dist = bfs(taxi_x-1,taxi_y-1,-1)
    if fuel-dist<0 or found==0:
        flag = False
        break
    else:
        fuel-=dist
    completed[found-2]=1
    #손님찾으면 손님위치가 이제 시작위치,이후 목적지찾기시작
    
    taxi_y,taxi_x, to_y, to_x = passengers[found-2]
    dist = 1e9
    found = -1
    marr[taxi_y-1][taxi_x-1] = 0
    marr[to_y-1][to_x-1]=-2
    # distance(0,taxi_x-1,taxi_y-1,-2)
    found, dist = bfs(taxi_x-1,taxi_y-1,-2)
    # test()
    # print(dist, found)
    marr[to_y-1][to_x-1]=0
    taxi_y,taxi_x = to_y, to_x
    #연료 떨어질때까지 진행
    if fuel-dist<0 or found ==0:
        flag=False
        break
    else:
        fuel-=dist
        fuel+=dist*2
    


# #     pass
# for i in range(len(passengers)):
#     y = passengers[i][0]
#     x = passengers[i][1]
#     marr[y-1][x-1]=i+2

# marr[4][5]=-2
# test()
# distance(1, 3,4,-2)
if flag:
    print(fuel)
else:
    print(-1)