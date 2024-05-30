# 1로 만들기
from collections import deque
N = int(input())

def bfs(num):

    q = deque([(num,0)])

    while q:
        number, depth =q.popleft()
        if number==1:
            return depth
        if number%3 ==0:
            q.append((number//3, depth+1))
        if number%2==0:
            q.append((number//2, depth+1))
        q.append((number-1,depth+1))


print(bfs(N))    