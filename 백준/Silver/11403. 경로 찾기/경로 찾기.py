N = int(input())
adjmat = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adjmat[i][j]==0:
            adjmat[i][j]=1e6


for k in range(N):
    for i in range(N):
        for j in range(N):
            adjmat[i][j] = min(adjmat[i][j], adjmat[i][k] + adjmat[k][j])


for i in range(N):
    for j in range(N):
        if adjmat[i][j]==1e6:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()