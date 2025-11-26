SIZE = 100*1000+1

C, N = map(int,input().split())
ad_info = []
for _ in range(N):
    cost, people = map(int,input().split())
    ad_info.append((cost,people))

dp = [0]*(SIZE) #cost당 최대 사람수

for i in range(SIZE):
    for cost, people in ad_info:
        if i+cost<SIZE:
            dp[i+cost]=max(dp[i+cost],dp[i]+people)

answer = 0
for i in range(SIZE):
    if dp[i]>=C:
        answer = i
        break

print(answer)