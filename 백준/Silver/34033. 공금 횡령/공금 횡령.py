import sys;input=sys.stdin.readline
N,M=map(int,input().split())
normal = {}

for _ in range(N):
    name, price = input().split()
    normal[name]=int(price)

abnCnt=0
for _ in range(M):
    name, price=input().split()
    if normal.get(name,0)*105/100<int(price):
        abnCnt+=1
print(abnCnt)