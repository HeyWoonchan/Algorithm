
#트리의 지름
from collections import deque
import sys
sys.setrecursionlimit(10**6)
V = int(input())

# adj_mat=[[0]*V for _ in range(V)]
adj_list=[[] for _ in range(V)]

for i in range(V):
    inputarr=list(map(int,input().split()))
    node = inputarr[0]
    inputarr=inputarr[1:]
    # print(inputarr)
    if inputarr[0]==-1:
        continue
    for j in range(len(inputarr)//2):
        a,b = inputarr[j*2],inputarr[j*2+1]
        adj_list[node-1].append((a-1,b))
    
# print(*adj_mat,sep='\n')

# def bfs(v):
#     global V
#     visited=[0]*V
    
#     q = deque([(v,0)])
#     visited[v]=1
    
#     max_length = 0
#     while q:
#         u,length = q.popleft()
#         max_length= max(max_length,length)
#         for arr in adj_list[u]:
#             i,weight=arr
#             if visited[i]==0:
#                 q.append((i,length+weight))
#                 visited[i]=1
#     return max_length


visited=[0]*V
max_node,max_length_dfs=0,0
def dfs(node,length):
    global max_length_dfs,max_node
    visited[node]=1
    # print(node,length)
    if max_length_dfs<length:

        max_length_dfs=length
        max_node=node
    for a in adj_list[node]:
        i, weight=a
        if visited[i]==0:
            dfs(i,length+weight)
max_length = 0
dfs(0,0)
visited=[0]*V
dfs(max_node,0)
    

print(max_length_dfs)