from collections import deque

def bfs(nowNode, visited, graph):
    q = deque([nowNode])
    visited[nowNode]=1
    
    while q:
        nowNode = q.popleft()
        
        for nextNode in range(len(graph[nowNode])):
            if graph[nowNode][nextNode]==1 and visited[nextNode]==0:
                visited[nextNode]=1
                q.append(nextNode)

def solution(n, computers):
    visited=[0]*n
    answer = 0
    for i in range(n):
        if visited[i]==0:
            bfs(i,visited,computers)
            answer+=1
    
    return answer