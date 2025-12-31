N = int(input())
arr=[tuple(map(int,input().split())) for _ in range(N)]
for i in range(len(arr)):
    t=0
    for j in range(len(arr)):
        if i==j:
            continue
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            t+=1
    print(t+1,end=' ')