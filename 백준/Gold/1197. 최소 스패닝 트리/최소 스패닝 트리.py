import heapq
V, E = map(int,input().split())

vertexs = [0]*(V+1)

graph = [[] for _ in range(V+1)]
for _ in range(E):
    A,B,C = map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

#Prim

nowEdges = []
selectedNodes = [0]*(V+1)
selectednodeset = set()
selectednodeset.add(1)
selectedEdge = 0
nowNode = 1
selectedNodes[1]=1
answer = 0
for nextNode, cost in graph[nowNode]:
    heapq.heappush(nowEdges,(cost,nextNode))
# print(nowEdges)
while nowEdges and selectedEdge<V-1:
    # print(nowEdges)

    cost, nowNode = heapq.heappop(nowEdges)
    # print("now selected node",nowNode)
    # selectedNodes[nowNode]=1
    if nowNode in selectednodeset:
        continue
    
    selectednodeset.add(nowNode)
    answer+=cost
    selectedEdge+=1

    for nextNode, nextCost in graph[nowNode]:
        if nextNode in selectednodeset:
            continue
        heapq.heappush(nowEdges, (nextCost, nextNode))

print(answer)
        