import sys
input = sys.stdin.readline
N = int(input())
exist = {}
arr = list(map(int,input().split()))
for a in arr:
    exist[a]=1
M = int(input())
sArr = list(map(int,input().split()))
for s in sArr:
    if s in exist:
        print(1)
    else:
        print(0)