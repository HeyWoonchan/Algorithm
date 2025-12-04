N, X = map(int,input().split())
socksPrice = list(map(int,input().split()))
ans = 10**10
for i in range(N-1):
    ans = min(ans, (socksPrice[i]+socksPrice[i+1])*X)
print(ans)