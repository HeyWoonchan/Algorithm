def preorder(node):
    if node =='.':
        return
    print(node,end="")
    preorder(adj_list[node][0])
    preorder(adj_list[node][1])

def inorder(node):
    if node=='.':
        return
    inorder(adj_list[node][0])
    print(node,end="")
    inorder(adj_list[node][1])

def postorder(node):
    if node=='.':
        return
    postorder(adj_list[node][0])
    postorder(adj_list[node][1])
    print(node,end="")

N = int(input())

adj_list= dict()

for _ in range(N):
    node, left, right = input().split()
    adj_list[node]=(left,right)

preorder('A');print()
inorder('A');print()
postorder('A')