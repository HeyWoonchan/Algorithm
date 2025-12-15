import sys
input = sys.stdin.readline


G=int(input())
P=int(input())

occupy = [-1]*G

searchfirst = {}
for i in range(G):
    searchfirst[i]=i

# print(occupy)
remainPlane = P
for i in range(P):
    a = int(input())
    t =-1
    for j in range(searchfirst[a-1], -1,-1):
        
        if occupy[j]==-1:
            t=j
            searchfirst[a-1]=j-1
            break
    # print(a,"탐색중,",t)
    if not 0<=t<=a-1 or occupy[t]>-1:
        print(i)
        break
    occupy[t] = i
    remainPlane-=1
    # print(occupy)
if remainPlane==0:
    print(P)