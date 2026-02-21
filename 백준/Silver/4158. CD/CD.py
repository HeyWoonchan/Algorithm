import sys
input = sys.stdin.readline
while True:
    N, M = map(int,input().split())
    if (N,M)==(0,0):
        break
    cds = {}

    for _ in range(N):
        cdNum = int(input())
        cds[cdNum] = cds.get(cdNum,0)+1
    for _ in range(M):
        cdNum = int(input())
        cds[cdNum] = cds.get(cdNum,0)+1


    ans = 0
    for a in cds.values():
        if a>1:
            ans+=1
    print(ans)
