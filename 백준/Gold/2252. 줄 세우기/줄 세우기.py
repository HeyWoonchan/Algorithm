"""
위상정렬
진입점이 0인거부터 큐에 넣고
하나 뺌, 그거와 연결된 점의 진입점을 하나씩 제거,
진입점이 0이 된 것들 다시 넣음
"""
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())

phase = [[] for _ in range(N+1)]
indegrees = [0]*(N+1)
for _ in range(M):
    A, B = map(int,input().split())
    phase[A].append(B)
    indegrees[B]+=1

q = deque()

for i in range(1,N+1):
    if indegrees[i]==0:
        q.append(i)

 
ans = []
while len(ans)<N:
    nowNode = q.popleft()
    ans.append(nowNode)
    for node in phase[nowNode]:
        indegrees[node]-=1
        if indegrees[node]==0:
            q.append(node)

print(*ans)