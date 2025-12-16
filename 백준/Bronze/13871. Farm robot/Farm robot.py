N, C, S = map(int,input().split())
query = list(map(int,input().split()))
record = [0]*N
now = 0;record[0]=1

for q in query:
    if q==1:
        now=(now+1)%N
        record[now]+=1
    else:
        now=(now-1)%N
        record[now]+=1
print(record[S-1])