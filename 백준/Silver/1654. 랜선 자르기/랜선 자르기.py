import sys
input = sys.stdin.readline
K,N=map(int,input().split())
arr = [int(input()) for _ in range(K)]

l,r = 1,2**31-1
while l<=r:
    mid = (l+r)//2
    t = 0
    for a in arr:
        t+=a//mid
    if t>=N:
        l=mid+1
    else:
        r=mid-1

print(r)
