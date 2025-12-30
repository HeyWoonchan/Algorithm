E,S,M=map(int,input().split())
e,s,m=1,1,1
ans=1
while (e,s,m)!=(E,S,M):
    e+=1;s+=1;m+=1;ans+=1
    if e>15:
        e=1
    if s>28:
        s=1
    if m>19:
        m=1
    
print(ans)