N=int(input())
arr=[tuple(map(int,input().split())) for _ in range(N)]
a=sorted(arr,key=lambda x:(-x[0],x[1],x[2]))
print(arr.index(a[0])+1)