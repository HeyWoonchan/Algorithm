def solution(s):
    cnt=0
    zCnt=0
    while s!='1':
        oCnt = s.count('1')
        zCnt2= len(s)-oCnt
        zCnt+=zCnt2
        s = str(bin(oCnt))[2:]
        cnt+=1
    
    answer = [cnt,zCnt]
    return answer