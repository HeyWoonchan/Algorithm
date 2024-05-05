import sys
sys.setrecursionlimit(10**6)
T = int(input())

def dfs(x,y):
    global visited,marr
    visited[y][x]=1
    for i in range(4):
        dx,dy = d[i]
        nx, ny = x+dx, y+dy
        if not (0<=nx<M and 0<=ny<N):
            continue
        if visited[ny][nx]==0 and marr[ny][nx]==1:
            dfs(nx,ny)
for _ in range(T):
    M,N,K = map(int, input().split())

    marr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        marr[y][x]=1

    # print(*marr, sep='\n')
    # print()
    d = [(0,1),(1,0),(-1,0),(0,-1)]

    visited = [[0]*M for _ in range(N)]
    

    
        
    
    cnt = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x]==0 and marr[y][x]==1:
                dfs(x,y)
                cnt+=1
    # print(*visited, sep='\n')
    print(cnt)