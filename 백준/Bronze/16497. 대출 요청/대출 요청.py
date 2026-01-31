N = int(input())
booking = [tuple(map(int,input().split())) for _ in range(N)]
K = int(input())

days = [[] for _ in range(32)]
#1 for borrow,-1 for return
for b,re in booking:
    days[b].append(1)
    days[re].append(-1)


for i in range(1,32):
    for j in range(len(days[i])):
        if days[i][j]==1:
            K-=1
        else:
            K+=1
    if K<0:
        print(0)
        exit(0)
    
print(1)
    