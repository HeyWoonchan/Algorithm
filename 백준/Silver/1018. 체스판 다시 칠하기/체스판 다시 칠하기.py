M,N = map(int,input().split())

wFirst = []
for i in range(M):
    row =[]
    if i%2==0:
        for j in range(N):
            if j%2==0:
                row.append('W')
            else:
                row.append('B')
    else:
        for j in range(N):
            if j%2==0:
                row.append('B')
            else:
                row.append('W')
    wFirst.append("".join(row))

bFirst = []
for i in range(M):
    row =[]
    if i%2==0:
        for j in range(N):
            if j%2==0:
                row.append('B')
            else:
                row.append('W')
    else:
        for j in range(N):
            if j%2==0:
                row.append('W')
            else:
                row.append('B')
    bFirst.append("".join(row))


target=[input() for _ in range(M)]

wMin=float('inf')
for i in range(M-7):
    for j in range(N-7):
        wCnt=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if wFirst[k][l]!=target[k][l]:
                    wCnt+=1
        wMin=min(wMin,wCnt)

bMin=float('inf')
for i in range(M-7):
    for j in range(N-7):
        bCnt=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if bFirst[k][l]!=target[k][l]:
                    bCnt+=1
        bMin=min(bMin,bCnt)

print(min(wMin,bMin))