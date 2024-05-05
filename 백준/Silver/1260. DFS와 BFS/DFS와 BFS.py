#DFS와 BFS
from collections import deque
N, M, V = map(int, input().split())
vertexs = [tuple(map(int,input().split()))for _ in range(M)]


adj_mat = [[0]*N for _ in range(N)]

for vertex in vertexs:
    i,j =  vertex
    adj_mat[i-1][j-1],adj_mat[j-1][i-1]=1,1


visited = [0]*N

# print(vertexs)

# print(*adj_mat, sep="\n")

def dfs(u):
    for v in range(N):
        if visited[v]==0 and adj_mat[u][v]==1:
            visited[v]=1
            print(v+1, end=" ")
            dfs(v)


visited[V-1]=1
print(V,end=" ")
dfs(V-1)

print()      

def bfs(n):
    visited = [0]*N
    queue = deque([n])
    while queue:
        u = queue.popleft()
        if visited[u]==0:
            visited[u]=1
            print(u+1, end=" ")
        for v in range(N):
            if visited[v]==0 and adj_mat[u][v]==1:
                queue.append(v)

bfs(V-1)