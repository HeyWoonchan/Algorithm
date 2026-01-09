import sys
input=sys.stdin.readline
N,M=map(int,input().split())
INF=float('inf')
adj=[[INF]*N for _ in range(N)]


for _ in range(M):
    A,B=map(int,input().split())
    A-=1;B-=1
    adj[A][B]=1
    adj[B][A]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j])
bacon=INF
ans=100

for i in range(N):
    t=0
    for j in range(N):
        if adj[i][j]==INF:
            continue
        t+=adj[i][j]
    if t<bacon:
        bacon=t
        ans=i

print(ans+1)