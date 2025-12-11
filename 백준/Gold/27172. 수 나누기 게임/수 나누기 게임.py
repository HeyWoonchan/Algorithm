import sys
input=sys.stdin.readline
MAXINT = 1000001
#입력
N = int(input())
dp = [0]*MAXINT
numberExist = [0]*MAXINT

arr = list(map(int,input().split()))
for a in arr:
    numberExist[a]=1


"""
어떤 수도, 두번 등장하지 않는다. <--이 점을 공략하여, 최적화해야 할 것 같다.
bruteforce는 100000*100001/2번 수행해야 하나, 
1. a로 b를 나눴을 때 나머지가 0이라면, b의 모든 배수 또한 a로 나눌 때 나머지가 0
"""




for a in arr:
    for j in range(a*2,MAXINT, a):
        if numberExist[j]==1:
            dp[j]-=1
            dp[a]+=1

for a in arr:
    print(dp[a], end=' ')