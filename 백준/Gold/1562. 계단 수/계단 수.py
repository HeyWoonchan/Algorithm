N = int(input())

dp = [[[0]*(1024) for _ in range(N+1)] for _ in range(10)]
MOD = 1000000000

for i in range(1,10):
    dp[i][1][1<<i]=1

for j in range(2,N+1): # 현재 자리수
    for i in range(0,10): # 현재 끝자리 숫자
        for bit in range(1024): # 지금까지 온 숫자 집합(이전 방문 기록 집합)
            if i-1>=0:  # i-1에서 i로 온 경우
                dp[i][j][bit | 1 << i] += dp[i-1][j-1][bit]
            if i+1<10:
                dp[i][j][bit | 1 << i] += dp[i+1][j-1][bit]
            dp[i][j][bit | 1 << i]%=MOD

answer = 0
for i in range(10):
    answer+=dp[i][N][1023]
    answer%=MOD
print(answer)