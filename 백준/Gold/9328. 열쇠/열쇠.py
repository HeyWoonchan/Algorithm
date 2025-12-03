import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())

def checkDoor(s):
    if ord('A')<=ord(s)<=ord('Z'):
        return True
    return False


def bfs(r,c, board, visited, keys, H, W, earnedmap):
    keysAddedFlag =0
    if visited[r][c]==1:
        return 0, 0
    if checkDoor(board[r][c]):
        if keys[ord(board[r][c])-ord('A')]!=1:
            return 0,0
    elif board[r][c]!='.' and board[r][c]!='$':
        # print(board[r][c])
        if keys[ord(board[r][c])-ord('a')]==0:
            keysAddedFlag=1
        keys[ord(board[r][c])-ord('a')]=1
        
        # print("key add:", board[r][c])
    q = deque([(r,c)])
    visited[r][c]=1
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    sum = 0

    #문 탐색 완료 이후 키를 찾을 경우, 해당 문에서 다시 탐색할 수 있어야 함.
    doorList = [[] for _ in range(26)]
    
    while q:
        r, c = q.popleft()
        # print("탐색중:", board[r][c])
        if board[r][c]=='$' and earnedmap[r][c]==0:
            sum+=1
            earnedmap[r][c]=1
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if not (0<=nr<H and 0<=nc<W):
                continue
            if visited[nr][nc]==1:
               continue
            if board[nr][nc] == '.':
                q.append((nr,nc))
                visited[nr][nc]=1
            elif checkDoor(board[nr][nc]):
                if keys[ord(board[nr][nc])-ord('A')]==1:
                    q.append((nr,nc))
                    visited[nr][nc]=1
                else:
                    doorList[ord(board[nr][nc])-ord('A')].append((nr,nc))
            elif board[nr][nc]!='$' and board[nr][nc]!='*':
                # print(board[nr][nc])
                if keys[ord(board[nr][nc])-ord('a')]==0:
                    keysAddedFlag=1
                keys[ord(board[nr][nc])-ord('a')]=1
                q.append((nr,nc))
                for door in doorList[ord(board[nr][nc])-ord('a')]:
                    q.append((door[0], door[1]))

                visited[nr][nc]=1
            elif board[nr][nc]!='*':
                q.append((nr,nc))
                visited[nr][nc]=1

    return (sum, keysAddedFlag)





def main():
    h, w = map(int,input().split())
    board = [input() for _ in range(h)]
    keys = [0]*26 #열쇠 저장소
    keysAlready = input()
    if keysAlready!='0\n':
        # print(keysAlready)
        for i in range(len(keysAlready)-1):
            keys[ord(keysAlready[i])-ord('a')]=1
    
    #상근이의 진입 가능 장소 탐색(가장자리가 벽이 아닌 경우)
    entries = []
    for i in range(h):
        for j in range(w):
            if not (i==0 or i==h-1) and not (j==0 or j==w-1):
                continue
            if board[i][j]!='*':
                entries.append((i,j))
    
    
    earned = [[0]*w for _ in range(h)]
    ans = 0

    #열쇠를 새로 얻었다면 다시 진행. 새로 얻는 열쇠가 없을 때까지 진행.
    while True:
        redoFlag = False
        visited = [[0]*w for _ in range(h)]
        for r, c in entries:
            tmp, kFlag = bfs(r,c, board, visited, keys, h, w, earned)
            ans += tmp
            if kFlag:
                redoFlag = True
        if redoFlag==False:
            break
        # print("new key added, redo")
        

    print(ans)



    #print(entries)







if __name__=="__main__":
    for _ in range(TC):
        main()
