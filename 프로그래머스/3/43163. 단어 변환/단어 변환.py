from collections import deque


def solution(begin, target, words):
    visited = [0]*len(words)
    q = deque()
    q.append((begin,0))
    
    while q:
        nowstr,num = q.popleft()

        if nowstr==target:
            return num
        
        for i in range(len(words)):
            if visited[i]!=0 or words[i]==begin:
                continue
            cnt = 0
            for r, s in zip(words[i], nowstr):
                if r==s:
                    cnt+=1
            if cnt==len(nowstr)-1:
                visited[i]=1
                q.append((words[i],num+1))
    return 0