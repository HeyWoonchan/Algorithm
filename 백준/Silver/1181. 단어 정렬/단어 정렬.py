import sys
input= sys.stdin.readline
N = int(input())
arr = [input().rstrip() for _ in range(N)]
arr=list(set(arr))
arr.sort(key=lambda x:(len(x),x))
print(*arr,sep='\n')