import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))



#inorder한 결과가 주어지고
#postorder한 결과가 주어졌을 때

#preorder한 결과를 구하라

"""
1 2 3 - inorder
1 3 2 - postorder

l root, r
1. 2.  3

l r root.
1 3 2

3개일때는 특정 가능

postorder의 오른쪽 끝은 항상 최상단 루트노드임.

이를 활용해서 inorder에서 좌우를 나눔.
나누어진 길이를 이용해서 또 후위순회에서 다음 최상단 루트노드를 찾고 반복.

"""
inorderIndexes = [0]*(n+1) #inorder의 각 요소의 인덱스를 저장해두고 한 번에 찾아서 사용.
for i in range(n):
    inorderIndexes[inorder[i]]=i

def preorder(inStart, inEnd, postStart, postEnd):
    if inStart>inEnd or postStart>postEnd:
        return

    nowRoot = postorder[postEnd]

    l = inorderIndexes[nowRoot]-inStart
    r = inEnd-inorderIndexes[nowRoot]
    print(nowRoot,end=' ')
    preorder(inStart, inStart+l-1,postStart,postStart+l-1)
    preorder(inEnd-r+1, inEnd, postEnd-r,postEnd-1)

preorder(0,n-1,0,n-1)