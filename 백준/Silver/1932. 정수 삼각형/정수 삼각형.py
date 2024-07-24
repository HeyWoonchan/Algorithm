n = int(input())

dp= [[0]*n for _ in range(n)]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(len(nums)):
        dp[i][j]=nums[j]

# print(dp)
for i in range(n-2,-1,-1):
    for j in range(n-1):
        dp[i][j]=dp[i][j]+max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])

