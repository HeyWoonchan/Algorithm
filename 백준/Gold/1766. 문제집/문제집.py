import heapq
import sys
input = sys.stdin.readline

#입력부
N, M = map(int,input().split()) 
graph = [[] for  _ in range(N+1)]
indegrees = [0]*(N+1)
for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    indegrees[B]+=1


#위상정렬
#+ 난이도가 쉬운 것부터 풀어야 함.(heapq사용)
q = []

for i in range(1,N+1):
    if indegrees[i]==0:
        heapq.heappush(q,i)

answer = []
while q and len(answer)<N:
    nowNode = heapq.heappop(q)
    answer.append(nowNode)
    for nextNode in graph[nowNode]:
        indegrees[nextNode]-=1
        if indegrees[nextNode]==0:
            heapq.heappush(q,nextNode)

print(*answer)