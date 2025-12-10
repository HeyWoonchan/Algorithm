N = int(input())
arr = list(map(int,input().split()))
dp = [0]*N

for i in range(N):
    t = 0
    for j in range(i):
        if arr[j]>arr[i]:
            t = max(t, dp[j])
    dp[i]=t+1

print(max(dp))
