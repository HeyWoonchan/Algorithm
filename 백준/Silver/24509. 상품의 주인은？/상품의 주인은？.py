import heapq,sys
input = sys.stdin.readline
N = int(input())

alist = [];blist = [];clist=[];dlist=[]

for i in range(N):
    num, a,b,c,d = map(int,input().split())
    heapq.heappush(alist,(-a,num))
    heapq.heappush(blist,(-b,num))
    heapq.heappush(clist,(-c,num))
    heapq.heappush(dlist,(-d,num))

received = [0]*(N+1)

while alist:
    r, i = heapq.heappop(alist)
    if received[i]!=1:
        received[i]=1
        print(i,end=' ')
        break
while blist:
    r, i = heapq.heappop(blist)
    if received[i]!=1:
        received[i]=1
        print(i,end=' ')
        break
while clist:
    r, i = heapq.heappop(clist)
    if received[i]!=1:
        received[i]=1
        print(i,end=' ')
        break
while dlist:
    r, i = heapq.heappop(dlist)
    if received[i]!=1:
        received[i]=1
        print(i)
        break

    