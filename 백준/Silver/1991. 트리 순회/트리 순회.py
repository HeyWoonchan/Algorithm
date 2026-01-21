def Atoi(a):
    if a=='.':
        return -1
    return ord(a)-ord('A')
def itoa(n):
    return chr(n+ord('A'))


def inorder(node):
    if node==-1:
        return
    
    inorder(tree[node][0])
    print(itoa(node),end='')
    inorder(tree[node][1])

def preorder(node):
    if node==-1:
        return
    print(itoa(node),end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def postorder(node):
    if node==-1:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(itoa(node),end='')

N=int(input())
tree=[[-1]*2 for _ in range(N)]

for _ in range(N):
    name, l,r = map(Atoi,input().split())
    tree[name][0]=l
    tree[name][1]=r

preorder(0)
print()
inorder(0)
print()
postorder(0)