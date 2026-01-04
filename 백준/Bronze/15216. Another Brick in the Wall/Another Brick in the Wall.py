import sys
input = sys.stdin.readline
h,w,n = map(int,input().split())
brick = list(map(int,input().split()))

nowK = 0
for i in range(h):
    nowkSum=0
    for k in range(nowK,n):
        nowkSum+=brick[k]
        if nowkSum>=w:
            nowK=k+1
            break
    if nowkSum!=w:
        print("NO")
        exit(0)
print("YES")