import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
ex = {}
for a in arr:
    if a in ex:
        ex[a]+=1
    else:
        ex[a]=1
M = int(input())
cArr = list(map(int,input().split()))
for c in cArr:
    if c in ex:
        print(ex[c],end=' ')
    else:
        print(0,end=' ')