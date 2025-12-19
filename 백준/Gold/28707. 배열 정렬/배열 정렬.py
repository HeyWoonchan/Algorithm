"""
배열_정렬의 Docstring

바로 똑같은것을 안하도록 뽑으면 된다.
배열 최대 길이 8
조작 개수 최대 10
원소 최대 10

한 동작 할때마다 증가하는 수열인지 확인 가능

1 2 1 2 -> 한 동작마다. 수열이 history와 똑같아지는지 확인?
우선 최대 10개 동작에 대해서
1 2 1 2
2 1 2 3 
...
까지 뽑아지는지 확인하자.
만들 수 없는것 판단- 조작할 수 없는 요소가, 제 자리의 번호가 아닌 경우.

실행 전, target미리 뽑기.


..결국 알고리즘 분류 확인

자료 구조
그래프 이론
집합과 맵
최단 경로
해시를 사용한 집합과 맵
데이크스트라

말도안돼


핵심 아이디어 -> 배열의 상태 자체가 노드다?
그럼 간선은? 바꾸는 행위 자체가 간선? ㄷㄷ
모든 노드에 대해 다음 노드로 가는 간선이 있는 것.
이런다고 목표 노드까지의 최단거리가 찾아진다는 보장은 어떻게 하는가?
-> 다익스트라를 사용하면 된다.


"""
import heapq
INF = float('inf')
N = int(input())
originalArr = list(map(int,input().split()))
M = int(input())
controls = [tuple(map(int,input().split())) for _ in range(M)]

finalTarget = "".join(str(i) for i in sorted(originalArr))

dists = {}

pq = [(0, originalArr)] # (0, "1234")

ans = 0
while pq:
    #다음 노드를 만들어 cost와 함께 heap에 넣기
    nowCost, u= heapq.heappop(pq)
    uStr = "".join(str(i) for i in u)
    if uStr not in dists:
        dists[uStr]=nowCost
    elif nowCost>dists[uStr]:
        continue
    for a,b,cost in controls:
        nextNode = [i for i in u]
        nextNode[a-1], nextNode[b-1] = nextNode[b-1], nextNode[a-1]
        nStr = "".join(str(i) for i in nextNode)
        #print(u, "".join(nextNode))
        nCost = nowCost+cost
        if not nStr in dists or nCost<dists[nStr]:
            dists[nStr]=nCost
            heapq.heappush(pq,(nCost,nextNode))

if finalTarget in dists:
    print(dists[finalTarget])
else:
    print(-1)
    
    
