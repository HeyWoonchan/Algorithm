N = int(input())
maxTime = 0;minCode = float('inf')
for _ in range(N):
    T, B = map(int,input().split())
    maxTime = max(maxTime, T)
    minCode = min(minCode, B)

print((maxTime*minCode)%7 +1)