N,R,C=map(int,input().split())
length=2**N
# grid=[[0]*length for _ in range(length)]

cnt=0
def sol(r,c,l):
    global cnt
    if l==1:
        # grid[r][c]=cnt
        cnt+=1
        if (r,c)==(R,C):
            print(cnt-1)
            exit(0)
        return
    if r>R and c>C:
        return
    if (r<=R<r+l//2 and c<=C<c+l//2):
        cnt+=0
        sol(r,c,l//2)
    if (r<=R<r+l//2 and c+l//2<=C<c+l):
        cnt+=(l//2)**2
        sol(r,c+l//2,l//2)
    if (r+l//2<=R<r+l and c<=C<c+l//2):
        cnt+=((l//2)**2)*2
        sol(r+l//2,c,l//2)
    if (r+l//2<=R<r+l and c+l//2<=C<c+l):
        cnt+=((l//2)**2)*3
        sol(r+l//2,c+l//2,l//2)

sol(0,0,length)
# print(grid)
# print(grid[R][C])
