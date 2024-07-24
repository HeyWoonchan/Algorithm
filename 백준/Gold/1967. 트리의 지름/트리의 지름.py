import sys
sys.setrecursionlimit(10**6)
n = int(input())

adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int,input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

visited= [0]*(n+1)

maxcost, maxnode=0,0
def dfs(node,cost):
    global maxcost, maxnode
    visited[node]=1
    if cost>maxcost:
        maxcost = cost
        maxnode = node
    for nextnode, nextcost in adj_list[node]:
        if visited[nextnode]==0:
            dfs(nextnode, cost+nextcost)


dfs(1,0)
visited= [0]*(n+1)
dfs(maxnode,0)

print(maxcost)