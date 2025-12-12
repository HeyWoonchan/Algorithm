"""
사이클_게임의 Docstring

노드의 간선을 추가하다가, 사이클이 형성되면 게임을 종료.
간선을 추가하다가 사이클이 형성되었는지를 곧바로 체크하려면?
노드의 개수 3<=n<=500000
간선의 개수 3<=m<=1000000

0 1
1 2
0 2

아
union find?

둘 다 같은 head를 가리킨다면 사이클을 만들게 되어버림.
추가할때마다, 노드의 우두머리를 찾으면서, 

둘중 하나가 집합을 이루는 경우 - 나머지 하나를 집합에 추가

둘다 다른 집합을 이루는 경우, 두 집합을 합침

모두 같은 집합을 가리키는 경우, 사이클 발생.
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

parent = [-1]*n

def find(node):
    if parent[node]==-1:
        return node
    return find(parent[node])

def union(a, b):
    fa = find(a)
    fb = find(b)
    if fa==fb:
        return False
    #둘다 루트 노드일 경우

    parent[fb] = fa
    #부모를 이어주면 됨.


    return True
    
flag= 0    
# print(parent)
for i in range(m):
    a,b = map(int,input().split())
    # print(a,b,"를 이어줌")
    
    fa, fb = find(a), find(b)
    # print("fa,fa:",fa,fb)
    
    if union(a,b)==False:
        print(i+1)
        flag=1
        break
    
    # print(parent)
if flag==0:
    print(0)