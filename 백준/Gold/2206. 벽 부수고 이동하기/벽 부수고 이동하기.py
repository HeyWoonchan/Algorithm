from collections import deque
N ,M = map(int,input().split())

marr = [list(input()) for _ in range(N)]

# print(marr)

visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
def bfs():
    q = deque([(0,0,0)])
    visited[0][0][0]=1
    d = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        # print(q)
        r, c, wall = q.popleft()
        if (r,c)==(N-1,M-1):
            return visited[r][c][wall]
        for dr,dc in d:
            nr,nc = r+dr, c+dc
            if not (0<=nr<N and 0<=nc<M):
                continue
            if marr[nr][nc]=='0' and visited[nr][nc][wall]==0:
                visited[nr][nc][wall]=visited[r][c][wall]+1
                q.append((nr,nc,wall))
            elif marr[nr][nc]=='1' and wall==0 and visited[nr][nc][1]==0:
                visited[nr][nc][1]=visited[r][c][0]+1
                q.append((nr,nc,1))

    return -1
print(bfs())