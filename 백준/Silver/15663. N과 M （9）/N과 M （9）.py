N,M=map(int,input().split())
arr=sorted(list(map(int,input().split())))

used=[0]*N
st=[]
result=set()
def sol(depth):
    if depth==M:
        result.add(tuple(st))
        return
    for i in range(N):
        if used[i]==1:
            continue
        used[i]=1
        st.append(arr[i])
        sol(depth+1)
        used[i]=0
        st.pop()
sol(0)
result=sorted(list(result))
for a in result:
    print(*a)