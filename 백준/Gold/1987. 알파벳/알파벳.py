R, C = map(int,input().split())

marr = [list(input()) for _ in range(R)]


d = [(-1,0),(1,0),(0,1),(0,-1)]
# visited= [[0]*C for _ in range(R)]
max_len = 0
history = [0]*(26)
def dfs(r,c, length_before):
    global max_len
    nowalpha = ord(marr[r][c])-ord('A')
    if history[nowalpha]==1:
        return
    # visited[r][c]=1
    history[nowalpha]=1
    max_len = max(max_len, length_before+1)
    for dr, dc in d:
        nr, nc= r+dr, c+dc
        if not (0<=nr<R and 0<=nc<C):
            continue
        if history[ord(marr[nr][nc])-ord('A')] ==0  and marr[r][c]!= marr[nr][nc]:
            dfs(nr,nc,length_before+1)
    # visited[r][c]=0
    history[nowalpha]=0

dfs(0,0,0)

print(max_len)