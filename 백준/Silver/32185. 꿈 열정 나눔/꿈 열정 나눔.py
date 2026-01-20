N, M=map(int,input().split())
V0,P0,S0 = map(int,input().split())
JaewonStat=V0+P0+S0
student=[]
for i in range(N):
    v,p,s=map(int,input().split())
    student.append((-(v+p+s),i))
student.sort()

ans=[0]
for i in range(N):
    s,index=student[i]
    if -s>JaewonStat:
        continue
    if len(ans)+1<=M:
        ans.append(index+1)
print(*ans)
