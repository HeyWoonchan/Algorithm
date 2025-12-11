"""
간격이 작은 것 부터 계산해두고, 범위를 늘려 가며 최소가되는 경우를 뽑아서 올라감

"""
import sys
input= sys.stdin.readline
INF = float('inf')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

#dp[start][end] -> 첫행렬start~끝행렬end 곱하는 경우의 최솟값

for dist in range(1,N): #간격 1부터 N까지
    for s in range(N):
        if s+dist>=N:
            break
        dp[s][s+dist]=INF

        for t in range(s, s+dist):
            dp[s][s+dist] = min(dp[s][s+dist], dp[s][t]+dp[t+1][s+dist] + arr[s][0]*arr[t][1]*arr[s+dist][1])

print(dp[0][N-1])