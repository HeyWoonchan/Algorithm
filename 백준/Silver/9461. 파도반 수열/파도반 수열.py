dp=[0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11,101):
    dp.append(dp[i-1]+dp[i-5])
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
    
