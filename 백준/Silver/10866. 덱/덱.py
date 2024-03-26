import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque([])
for i in range(N):
    arr = list(sys.stdin.readline().split())
    if arr[0] == "push_front":
        Q.appendleft(arr[1])
    elif arr[0]=="push_back":
        Q.append(arr[1])
    elif arr[0] =="pop_front":
        if len(Q)==0:
            print(-1)
        else:
            print(Q.popleft())
    elif arr[0] =="pop_back":
        if len(Q)==0:
            print(-1)
        else:
            print(Q.pop())
    elif arr[0] == "size":
        print(len(Q))
    elif arr[0] == "empty":
        if len(Q)==0:
            print(1)
        else:
            print(0)
    elif arr[0] == "front":
        if len(Q)==0:
            print(-1)
        else:
            print(Q[0])
    elif arr[0] == "back":
        if len(Q)==0:
            print(-1)
        else:
            print(Q[-1])

