from collections import deque
A, B = map(int, input().split())

q = deque()
q.append((A,1))
flag = 1
while q:
    now,num = q.popleft()
    # print(now)
    if now==B:
        print(num)
        flag=0
        break
    for i in [now*2, now*10+1]:
        if i<=B:
            q.append((i,num+1))

if flag:
    print(-1)