N = int(input()) #체스판의 크기
chessMap = [list(map(int,input().split())) for _ in range(N)]


#최악의 경우- 2^100 탐색, 그러나 한 자리에 두는 순간 다음 후보는 대략 10~19칸이 없어짐. 따라서 지수 100은 유의미하게 작아지긴 하는데, 얼만큼인지는 ....
#메모리 제한은 128메가이므로, 맵을 모든 경우에 맞게 만들 수는 없음.
# 아. 대각선을 기준으로 하여 이미 놓은 대각선을 건너뛰면 아주 빠름..
# -> 한 자리에 놓는 순간, 그 대각선을 바로 건너뛸 수 있음.
crosses = [[] for _ in range(2*N-1)]
# for cross in range(2*N-1):
    
#     #대각 좌
#     r, c = 0,cross
#     while 0<=r<N and 0<=c<N:
#         if chessMap[r][c]==1:
#             crosses[cross].append((r,c))
#         r+=1
#         c-=1
#     if cross==N-1:
#         continue
#     #대각 우
#     r,c = N-1-cross, N-1
#     while 0<=r<N and 0<=c<N:
#         if chessMap[r][c]==1:
#             crosses[2*N-2-cross].append((r,c))
#         r+=1
#         c-=1
for r in range(N):
    for c in range(N):
        if chessMap[r][c]==1:
            crosses[r+c].append((r,c))

#r+c가 같은 것은 우상 대각선
#r-c가 같은 것은 우하 대각선
#백트래킹시 r+c에서 하나를 뽑으면, r-c도 못뽑는것.
rightdown = [0]*(2*N-1)

ans = 0
def sol(i,bishopCount): #i: 우상 대각선칸
    global ans
    if i>=2*N-1:
        ans = max(ans,bishopCount)
        return
    #더이상 살필 필요 없는 경우
    if ans>=bishopCount+2*N-1-i:
        return 
    #현재 대각선에 비숍을 놓는 경우
    for r, c in crosses[i]:
        if rightdown[r-c]==0: #우하 대각선에 놓은 상태라면 못 둠
            rightdown[r-c]=1
            sol(i+1,bishopCount+1)
            rightdown[r-c]=0

    #안놓고 다음 대각선
    sol(i+1,bishopCount)

sol(0,0)
print(ans)
    



