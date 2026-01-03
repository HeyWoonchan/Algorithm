from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    pArr = list(map(int,input().split()))
    pArr2 = []
    for i in range(N):
        pArr2.append((pArr[i],i))

    q = deque(pArr2)
    cnt=0
    while q:
        a, i = q.popleft()
        flag=0
        for d in q:
            if d[0]>a:
                q.append((a,i))
                flag=1
                break
        if flag==0:
            cnt+=1
            if i==M:
                break
        
    print(cnt)