import sys

N = int(input())
for _ in range(N):
    input()

ans = []
for i in range(N):
    if i%2==0:
        ans.append([1]*N)
    else:
        ans.append([2]*N)

for i in range(N):
    print(*ans[i])