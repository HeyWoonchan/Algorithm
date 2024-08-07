#15684
from collections import deque
N, M, H = map(int,input().split())

horiz = [tuple(map(int,input().split())) for _ in range(M)]

marr = [[-1]+[0]*(N) for _ in range(H+1)]

#놓을 수 있는 곳을 미리 뽑기
possibles = []
for i in range(1,H+1):
    for j in range(1,N):
        if marr[i][j]== 0 and marr[i][j+1]==0:
            possibles.append((i,j))

for a,b in horiz:
    marr[a][b]=b+1
    marr[a][b+1]=b

# print()
def down(start):
    col = start
    for i in range(1,H+1):
        if marr[i][col]!=0:
            col = marr[i][col]
        # print(col)
    return col

min_lines = 4
def sol2(num, a,b,c):
    global min_lines
    #지금 단계에 다리 놓고 확인
    marr[a][b]=b+1
    marr[a][b+1]=b

    flag =True
    for i in range(1,N+1):
        curr = down(i)
        if curr!=i:
            flag=False
            break
        
    if flag==True: #현재 단계가 통과했으면 min_lines 업데이트
        min_lines = min(min_lines, num)
    else: #실패한경우 다른 놓을 수 있는 곳에 방문
        for i in range(c,len(possibles)):
            j,k = possibles[i]
            if marr[j][k]== 0 and marr[j][k+1]==0:
                    if num+1<4 and marr[j][k]== 0 and marr[j][k+1]==0:
                        sol2(num+1,j,k,i+1)

    #지금단계가 끝나면 맵 되돌림
    marr[a][b]=0
    marr[a][b+1]=0
def sol():
    global min_lines
    q = deque()

    for i in range(len(possibles)):
        a,b = possibles[i]
        q.append((0,a,b))
    while q:
        num, a, b = q.popleft()
# sol([])
flag =True
for i in range(1,N+1):
    curr = down(i)
    if curr!=i:
        flag=False
        break

if flag==True:
    print(0)
else:
    for i in range(len(possibles)):
        a,b = possibles[i]
        if marr[a][b]== 0 and marr[a][b+1]==0:
            sol2(1,a,b,0)
    print(min_lines if min_lines!= 4 else -1)