N, K = map(int, input().split())

arr=[]
for i in range(1,N+1):
    arr.append(i)

print("<",end="")
j=K-1
for i in range(N-1):
    print("%d, "%arr[j%N], end="")
    arr[j%N]=-1
    for k in range(K):
        while arr[(j+1)%N]==-1:
            j+=1
        j+=1
print("%d>"%arr[j%N])
    

    
