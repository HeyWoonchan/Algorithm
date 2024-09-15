from collections import deque
def solution(maps):
    answer = 0
    
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    q = deque()
    
    visited[0][0]=1
    q.append((0,0,1))
    
    while q:
        r,c, cnt = q.popleft()
        if (r,c)==(len(maps)-1, len(maps[0])-1):
            return cnt
        
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr,nc = r+dr,c+dc
            if not (0<=nr<len(maps) and 0<=nc<len(maps[0])):
                continue
            if maps[nr][nc]==1 and visited[nr][nc]==0:
                visited[nr][nc]=1
                q.append((nr,nc,cnt+1))
        
    return -1