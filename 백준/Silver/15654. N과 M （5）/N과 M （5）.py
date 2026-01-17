N,M=map(int,input().split())
arr=sorted(list(map(int,input().split())))

st=[]
used=[0]*N
def sol(depth):
    if depth==M:
        print(*st)
        return
    for i in range(N):
        if used[i]==1:
            continue
        used[i]=1
        st.append(arr[i])
        sol(depth+1)
        st.pop()
        used[i]=0
sol(0)