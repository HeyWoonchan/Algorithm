import copy,sys
input = sys.stdin.readline
N = int(input())
map2048 = []
for _ in range(N):
    a = list(map(int,input().split()))
    map2048.append(a)

#1. left

# 이미 이번 단계에서 합쳐진 것들에 대해서, 더이상 합쳐지지 못하게 처리.
# -> 합쳐지면, 1개가 되고, 1개가 되는 위치에 flag를 세움.
# -> 다음것이 이것과 합쳐지려고 하면 flag를 체크하여 방지.



def left(graph):
    for row in range(N):
        flags = [0]*N
        for col in range(N):
            #moving map[row][col] stuff to map[row][0](left as possible)
            if graph[row][col]==0:
                continue
            i = col
            while i>=0:
                # look i-1 and see if there is a thing
                # if there is noting, move i to i-1, now i is i-1
                # if there is a thing, check if merge is possible
                # if possible, merge and flag on , end
                # end
                
                if i-1>=0 and graph[row][i-1]==0:
                    graph[row][i-1],graph[row][i] = graph[row][i],graph[row][i-1]
                elif i-1>=0 and graph[row][i-1] != graph[row][i]:
                    break
                elif i-1>=0 and graph[row][i-1] == graph[row][i] and flags[i]==0 and flags[i-1]==0:
                    graph[row][i-1]*=2
                    graph[row][i]=0
                    flags[i-1]=1
                    break
                i-=1
    return graph

def rotate90clock(board):
    board = list(map(list, zip(*board[::-1])))
    return board


def right(graph):
    for _ in range(2):
        graph = rotate90clock(graph)
    graph = left(graph)
    for _ in range(2):
        graph = rotate90clock(graph)
    return graph


def down(graph):
    
    for _ in range(1):
        graph = rotate90clock(graph)
    graph = left(graph)
    for _ in range(3):
        graph = rotate90clock(graph)
    return graph


def up(graph):
    for _ in range(3):
        graph = rotate90clock(graph)
    graph = left(graph)
    for _ in range(1):
        graph = rotate90clock(graph)
    return graph
# left()

# right()
# down()
ans = 0
#now we should bruteforce it.
def sol(depth, nowgraph,move):
    global ans
    
    # print('depth, moved',depth,move)
    # print(*nowgraph, sep='\n')
    # print()
    
    if depth==5:
        # print("depth 5")
        # print(*nowgraph,sep='\n')
        # print()
        for i in range(N):
            for j in range(N):
                ans = max(ans, nowgraph[i][j]) 
        return

    left_graph = left(copy.deepcopy(nowgraph))
    sol(depth+1, left_graph,"left")

    right_graph = right(copy.deepcopy(nowgraph))
    sol(depth+1, right_graph,"right")
    
    up_graph = up(copy.deepcopy(nowgraph))
    sol(depth+1, up_graph,"up")
    
    down_graph = down(copy.deepcopy(nowgraph))
    sol(depth+1, down_graph, "down")

sol(0,copy.deepcopy(map2048),"start")
print(ans)

# tmp = up(map2048)
# print(*left(map2048), sep='\n')
# print(*tmp, sep='\n')
# tmp = down(tmp)
# print(*tmp, sep='\n')