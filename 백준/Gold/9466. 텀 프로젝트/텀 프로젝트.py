import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


TC = int(input())

#탐색 시, 탈출조건은, 방문한 곳에 또 방문할 경우 탈출
#a지점에서 출발했다가 사이클이 그 밑에서 난 경우, 사이클 판단?

nowteam = 0

def dfs(depth, node, targets, visitedForNow, visitedTotal): 
    global nowteam
    #시작점으로부터, 탐색 후, 안에서 사이클을 형성했다면(이번 탐색에서 방문했던 것을 또방문), 그 사이클 내부 사람수를 리턴.
    # print("탐색:",node)
    visitedForNow[node]=depth
    visitedTotal[node]=1
    nextNode = targets[node]
    if visitedTotal[nextNode]==1 and visitedForNow[nextNode]==0: #이번 단계의 탐색이 아닌 이전 단계 탐색한 것을 방문할 필요는 없음
        # print("이전 탐색에서 방문함")
        nowteam = 0
        visitedForNow[node]=0
        return
    if visitedForNow[nextNode]==0:
        dfs(depth+1, nextNode, targets, visitedForNow, visitedTotal)
    else:
        # print("이번 탐색에서 방문한 node를 방문하려함:",nextNode,"depth:",depth)
        nowteam =  depth-visitedForNow[nextNode]+1
    visitedForNow[node]=0

def main():
    global nowteam
    n = int(input())
    targets = [0]+list(map(int,input().split()))
    
    visited=[0]*(n+1)
    answer = 0
    visitedForNow = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i]==0: #이전 단계에서 방문한 적이 없다면
            nowteam = 0
            dfs(1,i,targets,visitedForNow, visited)
            answer+=nowteam
    print(n-answer)    
    


if __name__=="__main__":
    for _ in range(TC):
        main()