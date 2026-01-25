while True:
    n = int(input())
    if n==0:
        break
    ans=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            ans+=i*j
    print(ans)