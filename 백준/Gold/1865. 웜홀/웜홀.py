import sys
input= lambda:sys.stdin.readline()
TC = int(input())

INF = int(1e9)

for _ in range(TC):
    
    N,M,W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S,E,-T))
    
    # print(edges)

    dist=[INF]*(N+1)
    def bellmanford(start):
        dist[start]=0
        for i in range(N):
            for j in range(len(edges)):
                curNode, nextNode, cost = edges[j]
                if dist[curNode]+cost<dist[nextNode]:
                    dist[nextNode]=dist[curNode]+cost
                    if i==N-1:
                        return False
        return True
    flag=1
    # for i in range(1,N+1):
    #     dist=[INF]*(N+1)
    #     result = bellmanford(i)
        
    #     if dist[i]<0:
    #         print("YES")
    #         flag=0
    #         break

    # if flag:
    #     print("NO")
    
    if bellmanford(1):
        print("NO")
    else:
        print("YES")