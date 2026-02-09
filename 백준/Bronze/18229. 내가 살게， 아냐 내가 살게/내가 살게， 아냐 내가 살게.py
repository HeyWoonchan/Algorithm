N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
reaches = [0]*N
for i in range(M):
    for j in range(N):
        reaches[j]+=A[j][i]
        if reaches[j]>=K:
            print(j+1,i+1)
            exit(0)