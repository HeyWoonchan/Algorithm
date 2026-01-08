import sys
input=sys.stdin.readline
N,M,B=map(int,input().split())
mapL=[list(map(int,input().split())) for _ in range(N)]
mapL1=[]
for i in range(N):
    mapL1+=mapL[i]
minL=mapL[0][0]
maxL=mapL[0][0]
for i in range(N):
    for j in range(M):
        minL=min(minL,mapL[i][j])
        maxL=max(maxL,mapL[i][j])
ans=float('inf')
height=0
for h in range(minL,maxL+1):
    blocks=B
    t=0
    for i in range(len(mapL1)):
        if mapL1[i]<h:
            t+=1*(h-mapL1[i])
            blocks-=h-mapL1[i]
        elif mapL1[i]>h:
            t+=2*(mapL1[i]-h)
            blocks+=mapL1[i]-h
    if blocks<0:
        continue
    if t<=ans:
        ans=t
        if h>height:
            height=h

print(ans,height)