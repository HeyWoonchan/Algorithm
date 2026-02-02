T = int(input())
for tc in range(T):
    print("Case #%d:"%(tc+1),end=' ')
    N = int(input())
    N*=2
    arr = list(map(int,input().split()))
    used = [0]*N
    for i in range(N-1):
        if used[i]==1:
            continue
        for j in range(i+1,N):
            # print("\n",arr[i],arr[j])
            if used[j]==1:
                continue
            if arr[i]//3*4==arr[j]:
                used[i]=1
                used[j]=1
                print(arr[i],end=' ')
                break
    print()