from collections import deque

def solution(n, edge):
    adj_list = [[] for _ in range(n+1)]
    for a,b in edge:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = [0]*(n+1)
    
    visited[1]=1
    q = deque([1])
    
    while q:
        cur_node = q.popleft()
        for next_node in adj_list[cur_node]:
            if visited[next_node]==0:
                visited[next_node]= visited[cur_node]+1
                q.append(next_node)

    return visited.count(max(visited))