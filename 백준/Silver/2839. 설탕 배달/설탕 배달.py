N = int(input())
ans = float('inf')
for i in range(2000):
    for j in range(1001):
        f = i*3+j*5
        if N==f:
            ans = min(ans,i+j)
if ans==float('inf'):
    print(-1)
else:
    print(ans)
