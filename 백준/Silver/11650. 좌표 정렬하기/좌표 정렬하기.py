import sys
input=sys.stdin.readline
N = int(input())
arr=[tuple(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[0],x[1]))
for x,y in arr:
    print(x,y)