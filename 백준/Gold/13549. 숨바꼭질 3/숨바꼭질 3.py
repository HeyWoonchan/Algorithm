from collections import deque
N, K = map(int, input().split())

q = deque()
q.append((N,0))
visited=[0]*100001
visited[N]=1
while q:
    # print(q)
    now, time = q.popleft()
    if now==K:
        print(time)
        break
    left=now-1
    right=now+1
    double=now*2
    if double<=100000 and visited[double]==0:
        visited[double]=1
        q.append((double,time))
    if left>=0 and visited[left]==0:
        visited[left]=1
        q.append((left, time+1))
    if right<=100000 and visited[right]==0:
        visited[right]=1
        q.append((right, time+1))






# INF = float('inf')
# dp = [INF]*100001
# dp[N]=0
# for i in range(N-1,-1,-1):
#     dp[i] = dp[i+1]+1

# for i in range(1,100000):
#     if i%2==0:
#         dp[i] = min(dp[i],dp[i-1]+1, dp[i//2], dp[i+1]+1)
#     else:
#         dp[i] = min(dp[i],dp[i-1]+1, dp[i+1]+1)
# dp[100000]= min(dp[100000],dp[50000], dp[99999]+1)

# for i in range(99999,0,-1):
#     if i%2==0:
#         dp[i] = min(dp[i],dp[i-1]+1, dp[i//2], dp[i+1]+1)
#     else:
#         dp[i] = min(dp[i],dp[i-1]+1, dp[i+1]+1)

# dp[0] =min(dp[0], dp[1]+1)

# for i in range(1,100000):
#     if i%2==0:
#         dp[i] = min(dp[i],dp[i-1]+1, dp[i//2], dp[i+1]+1)
#     else:
#         dp[i] = min(dp[i],dp[i-1]+1, dp[i+1]+1)

# dp[100000]= min(dp[100000],dp[50000], dp[99999]+1)
# print(dp[K])
