MAX = 101
grid = [[0]*MAX for _ in range(MAX)]

for _ in range(4):
    x1, y1, x2,y2 = map(int,input().split())
    for r in range(x1,x2):
        for c in range(y1,y2):
            grid[r][c]=1

ans = 0 
for i in range(MAX):
    for j in range(MAX):
        ans+=grid[i][j]

print(ans)