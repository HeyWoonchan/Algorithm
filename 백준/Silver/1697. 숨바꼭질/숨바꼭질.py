from collections import deque
N, K = map(int, input().split())

"""
바로 옆에서 한칸 갈수있는지, 아니면 *2했다가 올수있는지 확인
"""
visited=[0]*100001
def bfs(nowX):
    global K
    q = deque([(nowX,0)])
    visited[nowX]=1
    while q:
        now, depth = q.popleft()
        
        if now==K:
            return depth
        if 0<=now-1<=100000 and visited[now-1]==0:
            q.append((now-1,depth+1))
            visited[now-1]=1
        if 0<=now+1<=100000 and visited[now+1]==0:
            q.append((now+1,depth+1))
            visited[now+1]=1
        if 0<=now*2<=100000 and visited[now*2]==0:
            q.append((now*2,depth+1))
            visited[now*2]=1


print(bfs(N))