N = int(input())
t = 1
cnt = 0
while cnt!=N:
    cnt6 = 0
    t+=1
    nowT = t
    last = -1
    nowMax6 = 0
    while nowT:
        if nowT%10==6:
            if last!=6:
                last=6
            cnt6+=1
            if cnt6>=3:
                nowMax6 = max(nowMax6,cnt6)
        else:
            cnt6=0
            last=-1
        nowT//=10

    if nowMax6>=3:
        cnt+=1
    
    # break
print(t)