from collections import deque
n,m = map(int,input().split())

marr=[list(map(int,input().split()))for _ in range(n)]

result = [[0]*m for _ in range(n)]


q = deque([])
for y in range(n):
    for x in range(m):
        if marr[y][x] == 2:
            q.append((x,y,0))

d= [(1,0),(0,1),(-1,0),(0,-1)]

while q:
    x,y, dist = q.popleft()
    result[y][x] = dist
    for i in range(4):
        dx, dy = d[i]
        nx,ny = x+dx, y+dy
        if (0<=nx<m and 0<=ny<n) and marr[ny][nx]==1:
            q.append((nx,ny, dist+1))
            marr[ny][nx] = -1
for y in range(n):
    for x in range(m):
        if marr[y][x] == 1:
            result[y][x] = -1


for i in range(n):
    print(*result[i],end=' ')
    print()


