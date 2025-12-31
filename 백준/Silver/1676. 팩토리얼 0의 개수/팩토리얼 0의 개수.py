fac=[1,1]
N = int(input())
for i in range(2,N+1):
    fac.append(fac[i-1]*i)
ans = str(fac[N])
cnt=0
# print(ans)
for i in range(len(ans)-1,-1,-1):
    if ans[i]!='0':
        break
    cnt+=1
print(cnt)