"""
선분_그룹의 Docstring
ccw, 두 선분이 만난다 + 분리집합?


"""
import sys
input = sys.stdin.readline
def ccw(x1,y1, x2,y2, x3,y3):
    t1= (x2-x1)*(y3-y1)
    t2= (y2-y1)*(x3-x1)
    if t1-t2>0:
        return 1
    elif t1-t2==0:
        return 0
    else:
        return -1
  
N = int(input())

lines = list(tuple(map(int,input().split())) for _ in range(N))

parent = [-1]*N
groupCnt = [1]*N

def isMeet(x1, y1, x2, y2, x3, y3, x4, y4):
    # 선분1
    t1 = ccw(x1,y1,x2,y2,x3,y3)
    t2 = ccw(x1,y1,x2,y2,x4,y4)
    # 선분2
    t3 = ccw(x3,y3,x4,y4,x1,y1)
    t4 = ccw(x3,y3,x4,y4,x2,y2)
    if t1==t2==t3==t4==0:
        if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and min(y1,y2)<=max(y3,y4) and min(y3,y4) <=max(y1,y2):
            return True
        else:
            return False
    elif t1!=t2 and t3!=t4:
        return True
    else:
        return False

def find(n):
    r= n
    while parent[r]!=-1:
        r = parent[r]
    return r

def union(a,b):
    fa = find(a)
    fb = find(b)
    if fa<fb:
        parent[fa]=fb
        groupCnt[fb]+=groupCnt[fa]
        groupCnt[fa]=0
    elif fa>fb:
        parent[fb]=fa
        groupCnt[fa]+=groupCnt[fb]
        groupCnt[fb]=0
    # if fa!=fb:
    #     parent[fa]=fb
    #     groupCnt[fb]+=groupCnt[fa]
    #     groupCnt[fa]=1
for i in range(1,N):
    for j in range(i):
        x1, y1, x2, y2 = lines[j]
        x3, y3, x4, y4 = lines[i]
        # print("i:", lines[i])
        # print("j:", lines[j])

        #선분이 겹치는지 확인(ccw)

        #i-1, i의 라인이 겹친다면, union(i-1,i)
        if isMeet(x1, y1, x2, y2, x3, y3, x4, y4):
            # print("만남, j에 i 추가")
            union(j,i)
        # else:
        #     print("안만남")

    #만나지 않는 라인이라면, x
# print(parent)
# print(groupCnt)

ans = 0
for a in parent:
    if a==-1:
        ans+=1
print(ans)
print(max(groupCnt))

# print(isMeet(-1,-1,1,1,-2,-2,2,2))