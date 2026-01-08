import sys
input = sys.stdin.readline
N,M=map(int,input().split())
trees=list(map(int,input().split()))

l,r=0,1000000000
while l<=r:
    mid = (l+r)//2
    t = sum(a-mid if a>mid else 0 for a in trees)
    if t>=M:
        l=mid+1
    else:
        r=mid-1
print(r)