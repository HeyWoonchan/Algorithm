from collections import deque
N,M = map(int,input().split())
arr = [0]*101
sadari_dict={}
for _  in range(N):
    x,y = map(int,input().split())
    sadari_dict[x]=y
    arr[x]=y
snake_dict={}
for _ in range(M):
    u,v = map(int,input().split())
    snake_dict[u]=v
    arr[u]=v
now = 1


def bfs():
    visited= [0]*101
    q = deque([(1,0,'1 ')])
    # dice_min = 99999
    while q:
        now_pos, dice_num, route = q.popleft() 
        # print(now_pos, dice_num)
        if now_pos==100:
            print(dice_num)
        for i in range(1,7):
            next_pos = now_pos+i
            if next_pos>100:
                continue
            if arr[next_pos]!=0:
                next_pos = arr[next_pos]
                # print(next_pos)
            if visited[next_pos]==0:
                
                q.append((next_pos,dice_num+1, route+str(next_pos)+' '))
                visited[next_pos]=1
bfs()


#010 4941 2491