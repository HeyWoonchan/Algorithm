arr=list(map(int,input().split()))
count=[0]*11
bingo=-1
for a in arr:
    count[a%10]+=1
    if count[a%10]==10:
        bingo=a%10
if bingo==0:
    print(10)
else:
    print(bingo)