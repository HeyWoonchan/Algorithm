import sys
input = sys.stdin.readline
N = int(input())
# origintable = [list(map(int,input().split())) for _ in range(N)]
minT=[]
maxT=[]
for i in range(N):
    origintable=list(map(int,input().split()))
    if i==0:
        minT=[origintable[0],origintable[1],origintable[2]]
        maxT=[origintable[0],origintable[1],origintable[2]]
    if i>0:
        tmpmin=[minT[0],minT[1],minT[2]]
        tmpmin[0]=origintable[0]+min(minT[0],minT[1])
        tmpmin[1]=origintable[1]+min(minT[0],minT[1],minT[2])
        tmpmin[2]=origintable[2]+min(minT[1],minT[2])
        minT=[tmpmin[0],tmpmin[1],tmpmin[2]]

        tmpmax=[maxT[0],maxT[1],maxT[2]]
        tmpmax[0]=origintable[0]+max(maxT[0],maxT[1])
        tmpmax[1]=origintable[1]+max(maxT[0],maxT[1],maxT[2])
        tmpmax[2]=origintable[2]+max(maxT[1],maxT[2])
        maxT=[tmpmax[0],tmpmax[1],tmpmax[2]]
print(max(maxT),min(minT))