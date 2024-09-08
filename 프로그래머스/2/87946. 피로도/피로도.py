max_ = 0
def solution(k, dungeons):
    global max_
    visited = [0]*len(dungeons)
    
    def sol(_k, _dungeons, cnt):
        global max_
        # print(_k, cnt)
        max_ = max(max_,cnt)

        
        for i in range(len(_dungeons)):
            if not visited[i] and _k>=_dungeons[i][0]:
                visited[i]=1
                sol(_k-_dungeons[i][1], _dungeons, cnt+1)
                visited[i]=0
    
    sol(k,dungeons,0)
    
    return max_