import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# adj_list = [[] for _ in range(n+1)]

INF = float('inf')
adj_mat = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    # adj_list[a].append((b,c))
    adj_mat[a][b]=min(adj_mat[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if adj_mat[i][j]>adj_mat[i][k]+adj_mat[k][j]:
                adj_mat[i][j] = adj_mat[i][k]+adj_mat[k][j]
            if j==i:
                adj_mat[i][j]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if adj_mat[i][j]==INF:
            print(0, end=' ')
        else:
            print(adj_mat[i][j], end=' ')
    print()


