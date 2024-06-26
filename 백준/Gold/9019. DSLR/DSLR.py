#DSLR

#register, value = n

#D double n and %10000

#S n-=1 9999 if n was 0

#L 자릿수 회전 왼쪽으로

#R 자리수 오른쪽으로 회전

#시간제한 6초

#A에서 DSLR커맨드 조합하여 최소로 도달하는 명령어 구하고 출력


from collections import deque
import sys

def sol2(value, target):
    visited = [0]*10000
    q = deque([(value,'')]) 
    visited[value]=1
    while q:
        now_value, now_command = q.popleft()
        if now_value == target:
            return now_command
        
        
        D_val = 2*now_value % 10000
        if visited[D_val]==0:
            q.append((D_val,now_command+'D'))
            visited[D_val]=1

        S_val=0
        if now_value==0:
            S_val = 9999
        else:
            S_val =  now_value-1
        if visited[S_val]==0:
            q.append((S_val,now_command+'S'))
            visited[S_val]=1

        tmp = str(now_value)
        for _ in range(4):
            if len(tmp)<4:
                tmp='0'+tmp
        L_val = ''
        for i in range(1,len(tmp)):
            L_val+=tmp[i]
        L_val = int(L_val+tmp[0])

        if visited[L_val]==0:
            q.append((L_val,now_command+'L'))
            visited[L_val]=1

        R_val = tmp[-1]
        for i in range(len(tmp)-1):
            R_val+=tmp[i]
        R_val = int(R_val) 
        if visited[R_val]==0:
            q.append((R_val,now_command+'R'))
            visited[R_val]=1

T = int(sys.stdin.readline())
for _ in range(T):
    A,B = map(int, sys.stdin.readline().split())
    result = sol2(A,B)
    sys.stdout.writelines(result)
    sys.stdout.writelines('\n')