"""
전깃줄_2의 Docstring

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

trace=[0]*500001
ansArr = []

def bisearch(num):
    l,r = 0, len(dp)-1
    while l<=r:
        mid = (l+r)//2
        if dp[mid]>num:
            r=mid-1
        else:
            l=mid+1
    return l

dp=[arr[0]]
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

# 역추적 시작
cur = dp[-1]
while cur!=0:
    pre[connected[cur]]=-1
    cur = trace[cur]

#답 출력
print(N-len(dp))
for i in range(1,500001):
    if pre[i]>0:
        print(i)