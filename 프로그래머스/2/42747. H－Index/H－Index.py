def solution(citations):
    citations.sort()
    
    #h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되는 h의 최댓값
    for i in range(0,len(citations)):
        if citations[i]>=len(citations)-i:
            return len(citations)-i
            
    
    return 0