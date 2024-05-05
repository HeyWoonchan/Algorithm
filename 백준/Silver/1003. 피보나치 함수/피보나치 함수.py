T = int(input())

dp_0 = [0]*41
dp_1 = [0]*41

for i in range(41):
    if i ==0:
        dp_0[i]=1
        dp_1[i]=0
    elif i==1:
        dp_0[i]=0
        dp_1[i]=1
    else:
        dp_0[i]=dp_0[i-1]+dp_0[i-2]
        dp_1[i]=dp_1[i-1]+dp_1[i-2]


for _ in range(T):
    n = int(input())
    print(dp_0[n], dp_1[n])


