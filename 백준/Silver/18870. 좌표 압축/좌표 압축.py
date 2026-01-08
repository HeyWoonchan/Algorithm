import sys,bisect
input=sys.stdin.readline
N = int(input())
xArr=list(map(int,input().split()))
XArrSorted=sorted(list(set(xArr)))
result={}

for a in XArrSorted:
    result[a]=bisect.bisect_left(XArrSorted,a)
for a in xArr:
    print(result[a],end=' ')
