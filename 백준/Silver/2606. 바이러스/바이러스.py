# 바이러스

from collections import deque

num_computers = int(input())
num_connections = int(input())


graph = [[0]*num_computers for _ in range(num_computers)]
for i in range(num_connections):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] =1

visited = [0]*num_computers

def bfs(num):
    global visited
    q = deque([num])
    visited[num] = 1
    
    while q:
        u = q.popleft()

        for v in range(num_computers):
            if visited[v]!= 1 and graph[u][v]==1:
                q.append(v)
                visited[v]=1
    
bfs(0)
print(sum(visited)-1)
