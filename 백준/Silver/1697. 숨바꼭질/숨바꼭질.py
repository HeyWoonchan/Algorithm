from collections import deque
N,K=map(int,input().split())

q=deque([(N,0)])
visited=[0]*100001
visited[N]=1

while q:
    x,t=q.popleft()
    if x==K:
        print(t)
        break
    
    if x-1>=0 and visited[x-1]==0:
        visited[x-1]=1
        q.append((x-1,t+1))
    if x+1<=100000 and visited[x+1]==0:
        visited[x+1]=1
        q.append((x+1,t+1))
    if 2*x<=100000 and visited[2*x]==0:
        visited[x*2]=1
        q.append((x*2,t+1))
    


    