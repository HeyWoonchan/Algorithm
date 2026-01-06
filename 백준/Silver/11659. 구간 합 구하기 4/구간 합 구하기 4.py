import sys
input= sys.stdin.readline
n,m=map(int,input().split())
arr = list(map(int,input().split()))
sums=[0,arr[0]]
for i in range(1,len(arr)):
    sums.append(sums[-1]+arr[i])
for _ in range(m):
    i,j=map(int,input().split())
    print(sums[j]-sums[i-1])