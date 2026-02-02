import sys
input = sys.stdin.readline
n,m=map(int,input().split())
used = [0]*(n+1)
req = [-1]*(n+1)
reqSet=set()
for i in range(m):
    a = int(input())
    req[a]=i
    reqSet.add(a)
cntReqNum = len(reqSet)
reqUnique = sorted(list(reqSet),key=lambda x:req[x])

while reqUnique:
    a = reqUnique.pop()
    print(a)
    used[a]=1

for i in range(1,n+1):
    if used[i]==1:
        continue
    print(i)
# print(used)