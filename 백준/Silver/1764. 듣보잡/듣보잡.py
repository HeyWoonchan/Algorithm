import sys
input = sys.stdin.readline
N, M =map(int,input().split())
names={}
for _ in range(N):
    a = input().rstrip()
    names[a]=1
dup=[]
for _ in range(M):
    a = input().rstrip()
    if a in names:
        dup.append(a)
print(len(dup))
dup.sort()
print(*dup, sep='\n')
    