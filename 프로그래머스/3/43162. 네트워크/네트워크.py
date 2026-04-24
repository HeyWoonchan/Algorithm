def dfs(nowNode, visited, graph,n):
    for i in range(n):
        if i==nowNode:
            continue
        if visited[i]==1:
            continue
        if graph[nowNode][i]==1:
            visited[i]=1
            dfs(i,visited,graph,n)


def solution(n, computers):
    visited=[0]*n
    answer = 0
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            answer+=1
            dfs(i,visited,computers,n)
            
    
    
    return answer