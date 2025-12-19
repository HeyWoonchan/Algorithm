N, K =map(int,input().split())
ans = 0;cur = N
for _ in range(K):
    ans = max(ans, int(str(cur)[::-1]))
    cur+=N
print(ans)