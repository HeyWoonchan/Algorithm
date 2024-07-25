import sys
input = sys.stdin.readline

N = int(input())

maxarr = list(map(int, input().split()))
minarr = [maxarr[0],maxarr[1],maxarr[2]]

for i in range(N-1):
    t1,t2,t3 = map(int,input().split())
    maxarr = [t1+max(maxarr[0],maxarr[1]), t2+max(maxarr),t3+max(maxarr[1],maxarr[2])]
    minarr = [t1+min(minarr[0],minarr[1]),t2+min(minarr),t3+min(minarr[1],minarr[2])]
    
print(max(maxarr), min(minarr))