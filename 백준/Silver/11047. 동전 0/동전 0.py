N, K= map(int,input().split())
coins = [int(input()) for _ in range(N)]
ans=0
now=0
for i in range(N-1,-1,-1):
    # print(now,((K-now)//coins[i]))
    if (K-now)//coins[i]==0:
        continue
    if now>=K:
        break
    ans+=((K-now)//coins[i])
    now += coins[i]*((K-now)//coins[i])
print(ans)