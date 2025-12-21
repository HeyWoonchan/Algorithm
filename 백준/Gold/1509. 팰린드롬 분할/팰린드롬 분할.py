import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline
INF = float('inf')

inputStr = input().rstrip()
length = len(inputStr)

pelinedrome = [[0]*length for _ in range(length)]

#미리 시간 안에 i~j까지의 pelindrome 여부를 만들 수가 있었음..

for i in range(length):
    pelinedrome[i][i]=1

for i in range(length-1):
    pelinedrome[i][i+1] = 1 if inputStr[i]==inputStr[i+1] else 0

for l in range(3,length+1):
    for s in range(length-l+1):
        e = s+l-1
        if inputStr[s]==inputStr[e] and pelinedrome[s+1][e-1]==1:
            pelinedrome[s][e]=1

dp = [INF]*length
for i in range(length):
    if pelinedrome[0][i]==1:
        dp[i]=0
    else:
        dp[i]=i
        for j in range(i+1):
            if pelinedrome[j][i]==1:
                dp[i]=min(dp[i],dp[j-1]+1)
print(dp[-1]+1)
