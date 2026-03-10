import math
N = int(input())
arr = list(map(int,input().split()))
k = int(input())
x = 1
for i in range(N):
    if N==k:
        break
    x*=2
    N//=2
# x개씩 sort한 결과값 출력

for i in range(0,len(arr),x):
    print(*sorted(arr[i:i+x]),end=' ')

#N//2 = 2개씩
#N//2 //2 4개씩
