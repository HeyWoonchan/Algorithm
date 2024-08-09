#20058
from collections import deque
N, Q = map(int,input().split())
length =2**N

marr = [list(map(int,input().split())) for _ in range(length)]

L_arr = list(map(int,input().split()))



def rotate_90(arr):
    return list(map(list,zip(*arr[::-1])))

def rotate(L):
    #한번에 건너뛸 칸수
    jump = 2**L

    for i in range(0,length, jump):
        for j in range(0,length, jump):
            # print("현재 왼쪽위 좌표:", i,j)
            # rotated = rotate_90(marr[i:i+jump][j:j+jump])
            rotated = rotate_90([marr[l][j:j+jump] for l in range(i,i+jump)])
            # print(*rotated, sep='\n')
            # print("회전배열 생성")
            for k in range(0, jump):
                for l in range(0,jump):
                    # print(k,l)
                    marr[i+k][j+l]=rotated[k][l]
    
#얼음작업
def ice():
    tmparr = [[0]*length for _ in range(length)]
    for r in range(length):
        for c in range(length):
            if marr[r][c]==0:
                continue
            cnt = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc = r+dr,c+dc
                if not (0<=nr<length and 0<=nc<length):
                    continue
                if marr[nr][nc]>=1:
                    cnt+=1
            if cnt>=3:
                tmparr[r][c]=marr[r][c]
            else:
                tmparr[r][c]=marr[r][c]-1
    return tmparr

visited=[[0]*length for _ in range(length)]
#덩어리찾기
def bfs(r,c):
    visited[r][c]=1

    q = deque([(r,c)])
    cnt = 0
    while q:
        now_r, now_c = q.popleft()
        cnt+=1
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = now_r+dr, now_c+dc
            if not (0<=nr<length and 0<=nc<length):
                continue
            if visited[nr][nc]==0 and marr[nr][nc]!=0:
                q.append((nr,nc))
                visited[nr][nc]=1
    return cnt


#전체작업시작
for L in L_arr:
    rotate(L)
    # print(*marr ,sep='\n')
    marr = ice()

#얼음덩어리 구하기
max_ices = 0
for r in range(length):
    for c in range(length):
        if marr[r][c]!=0 and visited[r][c]==0:
            cnt = bfs(r,c)
            max_ices = max(max_ices, cnt)

print(sum(sum(i) for i in marr))
print(max_ices)