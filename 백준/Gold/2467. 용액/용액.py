N = int(input())
solutions = list(map(int,input().split()))
MAXNUM = 1000000000*3


l,r =0, N-1
minAbs = MAXNUM
answer = []
while l<r:
    nowsum = solutions[l]+solutions[r]
    if abs(nowsum)<minAbs:
        answer = [solutions[l],solutions[r]]
        minAbs=abs(nowsum)
    
    if nowsum>0:
        r-=1
    else:
        l+=1



print(*answer, sep=' ')