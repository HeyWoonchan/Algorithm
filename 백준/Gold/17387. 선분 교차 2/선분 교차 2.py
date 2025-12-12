"""
선분_교차_2의 Docstring

 
"""

def ccw(x1,y1, x2, y2, x3, y3):
    t1 = (x2-x1)*(y3-y1)
    t2 = (x3-x1)*(y2-y1)
    if t1-t2>0:
        return 1
    elif t1-t2==0:
        return 0
    else:
        return -1
    
#입력
x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

#L1을 기준으로, L2양 끝점에 대해 CCW
fromL1toL2a = ccw(x1,y1,x2,y2,x3,y3)
fromL1toL2b = ccw(x1,y1,x2,y2,x4,y4)



#L2를 기준으로, L1양 끝점에 대해 CCW
fromL2toL1a = ccw(x3,y3,x4,y4,x1,y1)
fromL2toL1b = ccw(x3,y3,x4,y4,x2,y2)

# print(fromL1toL2a,fromL1toL2b)
# print(fromL2toL1a,fromL2toL1b)

#모두 일직선 상에 있을 경우
if fromL1toL2a==fromL1toL2b==fromL2toL1a==fromL2toL1b==0:
    #한 선분 위 한 점이, 다른 선분의 범위 내에 있다면 겹치는 것
    if min(x1,x2)<=max(x3,x4) and max(x1, x2)>=min(x3,x4) and min(y1,y2) <= max(y3,y4) and max(y1,y2)>=min(y3,y4):
        print(1)
    else:
        print(0)
elif fromL1toL2a!=fromL1toL2b and fromL2toL1a!=fromL2toL1b:
    print(1)
else:
    print(0)
