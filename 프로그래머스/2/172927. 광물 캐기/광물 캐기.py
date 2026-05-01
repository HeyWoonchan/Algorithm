minTired = 100000000
tiredTable=[]
tiredTable.append({"diamond":1,"iron":1,"stone":1})
tiredTable.append({"diamond":5,"iron":1,"stone":1})
tiredTable.append({"diamond":25,"iron":5,"stone":1})



def sol(nowMineralIdx, nowPickCnt, nowPickIdx, nowTired, minerals,picks):
    global minTired
    if nowMineralIdx>=len(minerals):
        minTired = min(minTired,nowTired)
        return
    # print(nowMineralIdx, nowPickCnt, nowPickIdx, nowTired)
    if (nowPickCnt<4):
        if nowMineralIdx+1<len(minerals):
            sol(nowMineralIdx+1,nowPickCnt+1, nowPickIdx, nowTired+tiredTable[nowPickIdx][minerals[nowMineralIdx+1]],minerals,picks)
        else:
            minTired = min(minTired,nowTired)
    else:
        if nowMineralIdx+1<len(minerals):
            flag=0
            for i in range(3):
                if picks[i]-1>=0:
                    flag=1
                    picks[i]-=1
                    sol(nowMineralIdx+1,0,i,nowTired+tiredTable[i][minerals[nowMineralIdx+1]],minerals,picks)
                    picks[i]+=1
            if flag==0:
                minTired = min(minTired,nowTired)
        else:
            minTired = min(minTired,nowTired)
def solution(picks, minerals):
    global minTired
    # print(tiredTable)
    sol(-1,5,0,0,minerals,picks)
    return minTired