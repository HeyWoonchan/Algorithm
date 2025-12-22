"""
전깃줄_2의 Docstring

겹치지 않는다의 조건은
2 2
6 4
7 6
9 7
10 10

왼쪽을 1부터 순서대로 본다면, 연결되는 우측의 번호가 오름차순이어야 한다
전깃줄을 제거했을 때, 오름차순이 이루어지도록 하기 위해 없애야 하는 최소 개수를 구하라.+무엇을 없애야 하는지.

1 2 3 4 5 6 7 8 9 10
8 2 9 

-> 가장 긴 증가하는 부분 수열 찾기.+trace
dp[i]=길이가 i인 최장 수열의 마지막 값.
새로운 마지막 값이 갱신될 때는 같이 감.->이것을 이용해서 되찾음.
복원한 것 이외의 것을 출력
"""

import sys
input = sys.stdin.readline


N = int(input())
connected = [0]*500001
pre = [0]*500001
arr = []
for _ in range(N):
    a,b = map(int,input().split())
    pre[a]=b
    connected[b]=a

for i in range(1,500001):
    if pre[i]>0:
        arr.append(pre[i])

dp=[arr[0]]
trace=[0]*500001

def bisearch(num):
    l,r = 0, len(dp)-1
    while l<=r:
        mid = (l+r)//2
        if dp[mid]>num:
            r=mid-1
        else:
            l=mid+1
    return l
ansArr = []
for i in range(1,N):
    if dp[-1]<arr[i]:
        trace[arr[i]] = dp[-1]
        dp.append(arr[i])
    else:
        j = bisearch(arr[i])
        if dp[j]>arr[i]:
            dp[j]=arr[i]
            if j==0:
                trace[arr[i]]=0
            else:
                trace[arr[i]]=dp[j-1]

cur = dp[-1]
# preAnswer = []

while cur!=0:
    # preAnswer.append(cur)
    pre[connected[cur]]=-1
    cur = trace[cur]

print(N-len(dp))

for i in range(1,500001):
    if pre[i]>0:
        print(i)


# print(preAnswer)
#     print(dp)
# print(dp)
# print(len(dp))
# print(ans)




