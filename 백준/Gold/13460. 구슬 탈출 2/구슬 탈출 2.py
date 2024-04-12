import copy
from collections import deque
N, M = map(int, input().split())


oririn_map_arr= [list(input())for _ in range(N)]

def left(map_arr):
    #각 행마다 옮겨줘야함
    for r in range(N):
        for c in range(M):
            if map_arr[r][c] == 'R' or map_arr[r][c]=='B':
                now_r, now_c = r,c
                while True:
                    nr,nc = now_r, now_c-1
                    if map_arr[now_r][now_c]=='R' and map_arr[nr][nc]=='O':
                        #동시에 들어가야 하는 경우까지 체크
                        check_r,check_c = r,c
                        while True:
                            check_r, check_c = check_r, check_c+1
                            if map_arr[check_r][check_c] == '#':
                                break
                            if map_arr[check_r][check_c] == 'B':
                                # 동시에 들어오는 파랑 구슬이 존재할경우 탐색실패
                                return 2
                        # 1 -> 뒤따라 들어오는 파랑구슬도 없고 성공! 탐색종료 명령주기
                        return 1
                    if map_arr[now_r][now_c]=='B' and map_arr[nr][nc]=='O':
                        # 2 -> 못하니까 이전 단계로 돌아가야함
                        return 2
                    if map_arr[nr][nc] != '.':
                        break
                    map_arr[now_r][now_c],map_arr[nr][nc] = map_arr[nr][nc],map_arr[now_r][now_c]
                    now_r,now_c=nr,nc
    # 0 -> 이동완료, 공 못빠져나감
    return 0

def right(map_arr):
    #각 행마다 옮겨줘야함
    for r in range(N-1,-1,-1):
        for c in range(M-1,-1,-1):
            if map_arr[r][c] == 'R' or map_arr[r][c]=='B':
                now_r, now_c = r,c
                while True:
                    nr,nc = now_r, now_c+1
                    if map_arr[now_r][now_c]=='R' and map_arr[nr][nc]=='O':
                        #동시에 들어가야 하는 경우까지 체크
                        check_r,check_c = r,c
                        while True:
                            check_r, check_c = check_r, check_c-1
                            if map_arr[check_r][check_c] == '#':
                                break
                            if map_arr[check_r][check_c] == 'B':
                                # 동시에 들어오는 파랑 구슬이 존재할경우 탐색실패
                                return 2
                        # 1 -> 뒤따라 들어오는 파랑구슬도 없고 성공! 탐색종료 명령주기
                        return 1
                    if map_arr[now_r][now_c]=='B' and map_arr[nr][nc]=='O':
                        # 2 -> 못하니까 이전 단계로 돌아가야함
                        return 2
                    if map_arr[nr][nc] != '.':
                        break
                    map_arr[now_r][now_c],map_arr[nr][nc] = map_arr[nr][nc],map_arr[now_r][now_c]
                    now_r,now_c=nr,nc
    return 0

def down(map_arr):
    #각 행마다 옮겨줘야함
    for c in range(M-1,-1,-1):
        for r in range(N-1,-1,-1):
            if map_arr[r][c] == 'R' or map_arr[r][c]=='B':
                now_r, now_c = r,c
                while True:
                    nr,nc = now_r+1, now_c
                    if map_arr[now_r][now_c]=='R' and map_arr[nr][nc]=='O':
                        #동시에 들어가야 하는 경우까지 체크
                        check_r,check_c = r,c
                        while True:
                            # print("check")
                            check_r, check_c = check_r-1, check_c
                            if map_arr[check_r][check_c] == '#':
                                break
                            if map_arr[check_r][check_c] == 'B':
                                # 동시에 들어오는 파랑 구슬이 존재할경우 탐색실패
                                return 2
                        # 1 -> 뒤따라 들어오는 파랑구슬도 없고 성공! 탐색종료 명령주기
                        return 1
                    if map_arr[now_r][now_c]=='B' and map_arr[nr][nc]=='O':
                        # 파란공이 먼저 들어가는경우
                        # 2 -> 못하니까 이전 단계로 돌아가야함
                        return 2
                    if map_arr[nr][nc] != '.':
                        break
                    map_arr[now_r][now_c],map_arr[nr][nc] = map_arr[nr][nc],map_arr[now_r][now_c]
                    now_r,now_c=nr,nc
    return 0
def up(map_arr):
    #각 행마다 옮겨줘야함
    for c in range(M):
        for r in range(N):
            if map_arr[r][c] == 'R' or map_arr[r][c]=='B':
                now_r, now_c = r,c
                while True:
                    nr,nc = now_r-1, now_c
                    if map_arr[now_r][now_c]=='R' and map_arr[nr][nc]=='O':
                        #동시에 들어가야 하는 경우까지 체크
                        check_r,check_c = r,c
                        while True:
                            check_r, check_c = check_r+1, check_c
                            if map_arr[check_r][check_c] == '#':
                                break
                            if map_arr[check_r][check_c] == 'B':
                                # 동시에 들어오는 파랑 구슬이 존재할경우 탐색실패
                                return 2
                        # 1 -> 뒤따라 들어오는 파랑구슬도 없고 성공! 탐색종료 명령주기
                        return 1
                    if map_arr[now_r][now_c]=='B' and map_arr[nr][nc]=='O':
                        # 2 -> 못하니까 이전 단계로 돌아가야함
                        return 2
                    if map_arr[nr][nc] != '.':
                        break
                    map_arr[now_r][now_c],map_arr[nr][nc] = map_arr[nr][nc],map_arr[now_r][now_c]
                    now_r,now_c=nr,nc
    return 0



#백트래킹으로 순서정하기 1:up, 2:down, 3:left, 4:right

min_steped = 11

def sol(step, marr, prevway):
    global min_steped
    if step==12:
        return
    
    for i in range(4):
        # print(i)
        new_arr = copy.deepcopy(marr)
        if i==0 and prevway!=1 and prevway!=0:
            # print("up!")
            result = up(new_arr)
            if result == 1:
                # print(step,"번만에 통과!, 마지막방향: 위")
                min_steped = min(min_steped, step+1)
                return
            elif result == 2:
                #이 스텝은 더이상 진행불가
                if prevway==-1:
                    continue
                else:
                    continue
                    return
            else:
                sol(step+1, new_arr,i)
        elif i==1 and prevway!=0 and prevway!=1:
            # print("down!")
            result = down(new_arr)
            if result == 1:
                min_steped = min(min_steped, step+1)
                # print(step,"번만에 통과!, 마지막방향: 아래")
                return
            elif result == 2:
                #이 스텝은 더이상 진행불가
                if prevway==-1:
                    continue
                else:
                    continue
                    return
            else:
                sol(step+1, new_arr,i)
        elif i==2 and prevway!=3 and prevway!=2:
            # print("left!")
            result = left(new_arr)
            if result == 1:
                min_steped = min(min_steped, step+1)
                # print(step,"번만에 통과!, 마지막방향: 왼쪽")
                return
            elif result == 2:
                #이 스텝은 더이상 진행불가
                if prevway==-1:
                    continue
                else:
                    continue
                    return
            else:
                sol(step+1, new_arr,i)
        elif i==3 and prevway!=2 and prevway!=3:
            # print("right!")
            result = right(new_arr)
            if result == 1:
                min_steped = min(min_steped, step+1)
                # print(step,"번만에 통과!, 마지막방향: 오른쪽")
                return
            elif result == 2:
                #이 스텝은 더이상 진행불가
                if prevway==-1:
                    continue
                else:
                    continue
                    return
            else:
                sol(step+1, new_arr,i)
    # print()
        

# def sol2(marr):

#     queue = deque([(0,-1)]) # step, prevway
#     while queue:
#         step, prevway = queue.popleft()
#         new_marr = copy.deepcopy(marr)
#         if step>9:
#             return -1
#         for i in range(4):
#             if i==0 and prevway!=1:
#                 result = up(new_marr)
#                 if result == 1:
#                     return step
#                 elif result == 2:
#                     #이 스텝은 더이상 진행불가
#                     continue
#                 else:
#                     queue.append((step+1,i))
#             elif i==1 and prevway!=0:
#                 result = down(new_marr)
#                 if result == 1:
#                     return step
#                 elif result == 2:
#                     #이 스텝은 더이상 진행불가
#                     continue
#                 else:
#                     queue.append((step+1,i))
#             elif i==2 and prevway!=3:
#                 result = left(new_marr)
#                 if result == 1:
#                     # min_steped = min(min_steped, step+1)
#                     return step
#                 elif result == 2:
#                     #이 스텝은 더이상 진행불가
#                     continue
#                 else:
#                     # sol(step+1, copy.deepcopy(marr),i)
#                     queue.append((step+1, i))
#             elif i==3 and prevway!=2:
#                 # print("right!")
#                 result = right(new_marr)
#                 if result == 1:
#                     # min_steped = min(min_steped, step+1)
#                     return step
#                 elif result == 2:
#                     #이 스텝은 더이상 진행불가
#                     continue
#                 else:
#                     # sol(step+1, copy.deepcopy(marr),i)
#                     queue.append((step+1, i))
#     return -1
    



sol(0,oririn_map_arr,-1)

if min_steped > 10:
    print(-1)
else:
    print(min_steped)

# ans = sol2(oririn_map_arr)
# print(ans)

# result = right(oririn_map_arr)
# result = down(oririn_map_arr)
# result = right(oririn_map_arr)
# result = up(oririn_map_arr)
# result = right(oririn_map_arr)
# result = down(oririn_map_arr)
# result = left(oririn_map_arr)
# result = up(oririn_map_arr)
# result = right(oririn_map_arr)
# result = down(oririn_map_arr)

# for i in range(N):
#     print(oririn_map_arr[i])

# print(result)