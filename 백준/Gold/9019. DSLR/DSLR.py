from collections import deque
import sys
input=sys.stdin.readline
T=int(input())
def bfs(now,target):
    q=deque([(now,'')])
    visited=[0]*10000
    visited[now]=1
    while q:
        now,hist = q.popleft()
        if now==target:
            return hist
        D = (now*2)%10000
        if visited[D]==0:
            visited[D]=1
            q.append((D,hist+'D'))
        if now==0:
            S=9999
        else:
            S=now-1
        if visited[S]==0:
            visited[S]=1
            q.append((S,hist+'S'))
        tmp = str(now)
        for _ in range(4):
            if len(tmp)<4:
                tmp='0'+tmp
        L = ''
        for i in range(1,len(tmp)):
            L+=tmp[i]
        L = int(L+tmp[0])
        if visited[L]==0:
            visited[L]=1
            q.append((L,hist+'L'))
        R_val = tmp[-1]
        for i in range(len(tmp)-1):
            R_val+=tmp[i]
        R_val = int(R_val) 
        if visited[R_val]==0:
            q.append((R_val,hist+'R'))
            visited[R_val]=1


for _ in range(T):
    A,B=map(int,input().split())
    print(bfs(A,B))
    