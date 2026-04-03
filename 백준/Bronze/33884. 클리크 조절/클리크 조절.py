import sys
input = sys.stdin.readline

N = int(input())
arr=sorted([tuple(map(int,input().split())) for _ in range(N)])
arr2=sorted([tuple(map(int,input().split())) for _ in range(N)])
print(arr2[0][0]-arr[0][0],arr2[0][1]-arr[0][1])
    