"""
할로윈의_양아치의 Docstring

N,M,K
c1~cN
a,b친구
~~
~~

스브러스가 친구의 사탕을 k를 넘지 않는 선에서 가장 많이 빼앗는 경우의 수?

1 2  3 4 5 6  7 8  9  10
9 15 4 4 1 5 19 14 20 5

1 3 - 1,3이 한묶음 -> 9+4=13
2 5 -> 15+


트리를 구성
부모노드를 a 로 하는 트리의 전체 사탕 수를 저장- > candies[a]=10
집합별 인원수도 저장.

정렬 후 


"""

import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int,input().split())
candiesReceived = list(map(int,input().split()))
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [0]*N


def bfs(node):
    sum = candiesReceived[node]
    people = 1
    q = deque([node])
    visited[node]=1
    while q:
        node = q.popleft()

        for nextnode in graph[node]:
            if visited[nextnode]==0:
                sum+=candiesReceived[nextnode]
                people+=1
                q.append(nextnode)
                visited[nextnode]=1
    return sum, people

arr = []
for i in range(N):
    if visited[i]==0:
        arr.append(bfs(i))
# arr.sort(key=lambda x:-x[0])


#인원이 k가 되기 전까지 가장 큰 것을 고르는 것
#점수,인원
#점수가 높은 순으로 채우는데도, 쪼갤 수 없다면 앞에것을 고르지 않고, 뒤의 작은것들로 더 큰 이득을 낼 수도 있음
#쪼갤 수 없으므로 DP로 해결 - 0-1 knapsack
"""
arr[i]를 고를 수도 있고 안고를 수도 있음
dp[k] -> k무게를 들기까지의 최대 무게?
arr[i]를 골랐을 경우, 안골랐을 경우
이전것을 고르고 넘어온 경우와ㅏ 안고르고 넘어온 경우 두가지?

dp[i][w] -> 물건을 i 까지 보았을 때, 최대 w까지의 무게 중 가장 큰 이득
dp[i][w] = max(dp[i-1][w](이전것을 안고르는 경우), dp[i-1][w-weight[i-1]]+value[i-1](고르는 경우))

"""
dp = [[0]*K for _ in range(len(arr)+1)]

for i in range(1,len(arr)+1):
    lvalue, lweight = arr[i-1]
    for w in range(1,K):
        if lweight<=w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-lweight]+lvalue)
        else:
            dp[i][w]=dp[i-1][w]
print(dp[len(arr)][K-1])