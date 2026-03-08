N,M = map(int,input().split())

first = [int(input()) for _ in range(N)]

second = [int(input()) for _ in range(M)]

table = []

for i in range(N):
    table.insert(first[i]-1,i)
secondTable=[]
for i in range(M-1,-1,-1):
    secondTable.insert(second[M-1-i]-1,table[i])
for a in secondTable[:3]:
    print(a+1)