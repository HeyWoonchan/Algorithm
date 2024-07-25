import sys
input = sys.stdin.readline

N = int(input())

maxarr = list(map(int, input().split()))
minarr = [maxarr[0],maxarr[1],maxarr[2]]

for i in range(N-1):
    t1,t2,t3 = map(int,input().split())

    max1 = t1+max(maxarr[0],maxarr[1])
    max2 = t2+max(maxarr[0],maxarr[1],maxarr[2])
    max3 = t3+max(maxarr[1],maxarr[2])

    maxarr = [max1, max2,max3]

    min1 = t1+min(minarr[0],minarr[1])
    min2 = t2+min(minarr[0],minarr[1],minarr[2])
    min3 = t3+min(minarr[1],minarr[2])
    minarr = [min1,min2,min3]
    
print(max(maxarr), min(minarr))
    


