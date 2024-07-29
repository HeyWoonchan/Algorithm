import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

parents = [0]*(N+1)

q = deque([1])

while q:
    node = q.popleft()

    for nextnode in adj_list[node]:
        if parents[nextnode]==0:
            parents[nextnode]=node
            q.append(nextnode)

print(*parents[2:], sep='\n')

