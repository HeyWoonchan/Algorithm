import heapq
from collections import deque
import sys
input=sys.stdin.readline
# 위상정렬
def main():
    N, K = map(int,input().split())
    node_time=[0]+list(map(int,input().split()))
    node_indegrees = [0]*(N+1)
    graph_map = [[] for _ in range(N+1)]

    for _ in range(K):
        X, Y = map(int,input().split()) #X->Y
        graph_map[X].append(Y) #Y->X
        node_indegrees[Y]+=1

    W = int(input())
    
    dp = [0]*(N+1)

    phasesorting = deque()
    
    for i in range(1,N+1):
        if node_indegrees[i]==0:
            phasesorting.appendleft(i)
    
    #진입차수가 0인 것 뽑기
    while phasesorting:
        zero_indegree = phasesorting.pop()
        #이 노드의 다음 노드 진입차수 1 제거
        for nextnode in graph_map[zero_indegree]:
            #다음노드 dp 의 값 설정
            dp[nextnode] = max(dp[nextnode], dp[zero_indegree]+node_time[zero_indegree])
            node_indegrees[nextnode]-=1
            if node_indegrees[nextnode]==0:
                phasesorting.appendleft(nextnode)

    print(dp[W]+node_time[W])    

if __name__=="__main__":

    T = int(input())
    for _ in range(T):
        main()
