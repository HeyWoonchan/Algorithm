from collections import deque
N,M = map(int,input().split())
arr = [0]*101
for _  in range(N):
    x,y = map(int,input().split())
    arr[x]=y
for _ in range(M):
    u,v = map(int,input().split())
    arr[u]=v
def bfs():
    visited= [0]*101
    q = deque([(1,0)])
    while q:
        now_pos, dice_num = q.popleft() 
        if now_pos==100:
            print(dice_num)
        for i in range(1,7):
            next_pos = now_pos+i
            if next_pos>100:
                continue
            if arr[next_pos]!=0:
                next_pos = arr[next_pos]
            if visited[next_pos]==0:
                q.append((next_pos,dice_num+1))
                visited[next_pos]=1
bfs()