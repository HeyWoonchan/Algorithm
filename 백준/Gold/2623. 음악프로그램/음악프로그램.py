#위상정렬
from collections import deque



#input
N, M = map(int,input().split())

adjMat = [[] for _ in range(N+1)]
indegrees = [0]*(N+1)

for _ in range(M):
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-1):
        adjMat[arr[i]].append(arr[i+1])
        indegrees[arr[i+1]]+=1

# print("indegrees:", indegrees)

#진입차수가 0인 노드 삽입
answer= []
q = deque()
for i in range(1, N+1):
    if indegrees[i]==0:
        q.append(i)

while q and len(answer)!=N:
    nowNode = q.popleft()
    answer.append(nowNode)
    for nextNode in adjMat[nowNode]:
        indegrees[nextNode]-=1
        if indegrees[nextNode]==0:
            q.append(nextNode)

print(*answer, sep='\n') if len(answer)==N else print(0)
    
