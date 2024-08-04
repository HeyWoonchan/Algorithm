n, m, r = map(int,input().split())
item_arr = list(map(int,input().split()))
INF = float('inf')
adj_mat = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,i= map(int,input().split())
    
    adj_mat[a][b]=i
    adj_mat[b][a]=i

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k]+adj_mat[k][j])
max_item = 0
for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if i==j:
            tmp+=item_arr[j-1]
        elif adj_mat[i][j]<=m:
            tmp+=item_arr[j-1]
    max_item=max(max_item,tmp)
print(max_item)
# print(*adj_mat,sep='\n')