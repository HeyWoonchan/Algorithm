"""
카드_게임의 Docstring
N 빨 M개 철수
N 파 M개 민수 같은 인덱스
낸 카드의 번호가 큰 사람이 이김
K번 해서 더 많이 번호가 큰 사람이 이김 - 한번 낸 것은 버림
철수 - 본인 카드 조작: 카드 버리고 다시 들고오거나 민수한테는 없는 카드 내기 가능
민수 - 철수가 낼 카드 알아냄: 철수가 낼 카드가 큰 카드 중 가장 작은 카드를 냄


10 7 5
2 5 3 7 8 4 9
4 1 1 3 8

4 -> 5 7 8 9, 5
2 3 7 8 4 9

1 -> 2 3 7 8 4 9, 2
3 7 8 4 9

이런식으로 
2 3 4 5 7 8 9에서, 바로 다음 수를 이미 고른 것을 제외하고 뽑아야함.
"""
import sys
input = sys.stdin.readline


N, M, K = map(int,input().rstrip().split())
cards = sorted(list(map(int,input().rstrip().split())))
cheolsu = list(map(int,input().rstrip().split()))

findNext = [i for i in range(M)]


def bisearch(num):
    l,r = 0,M-1
    while l<=r:
        mid = (l+r)//2
        if cards[mid]<num:
            l = mid+1
        else:
            r = mid-1
    return l

visited =[0]*M
for c in cheolsu:
    r = bisearch(c+1)
    for j in range(findNext[r],M):
        if cards[j]>c and visited[j]==0:
            print(cards[j])
            findNext[r]=j+1
            visited[j]=1
            break


