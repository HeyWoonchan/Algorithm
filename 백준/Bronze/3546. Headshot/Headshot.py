loaded = input()
n = len(loaded)
#방아쇠를 당기면 오른쪽으로 한칸 밀림
#010101 인 경우, 무조건 rotate 하는게 이득
#001001 0이 
#00101001
zeros=0
zeroBeforeOne = 0
for i in range(n):
    next = (i+1)%n
    if loaded[i]=='0':
        zeros+=1
        if loaded[next]=='1':
            zeroBeforeOne+=1
    
# print(zeroBeforeOne)
# print(zeros)
if zeros==n or zeros==zeroBeforeOne*2:
    print("EQUAL")
elif zeros<zeroBeforeOne*2:
    print("ROTATE")
else:
    print("SHOOT")