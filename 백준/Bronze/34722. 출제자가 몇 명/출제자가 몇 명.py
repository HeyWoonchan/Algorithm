N = int(input())

Boj = [0]*N
code = [0]*N
atcoder = [0]*N
icpc = [0]*N

for i in range(N):
    a,b,c,d = map(int,input().split())
    Boj[i]=a;code[i]=b;atcoder[i]=c;icpc[i]=d

ans= 0

for i in range(N):
    if Boj[i]>=1000 or code[i]>=1600 or atcoder[i]>=1500 or (1<=icpc[i]<=30):
        ans+=1

print(ans)