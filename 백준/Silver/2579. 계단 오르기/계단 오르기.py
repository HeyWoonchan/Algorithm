# 계단 오르기
N = int(input())
stair = [int(input()) for _ in range(N)]

dp2= [0]*(N+1)

for i in range(1,N+1):
    if i==1:
        dp2[i]=stair[i-1]
    elif i==2:
        dp2[i]=stair[i-1]+dp2[i-1]

    elif i==3:
        dp2[i]=stair[i-1]+max(stair[i-2],stair[i-3])
    else:
        dp2[i] = stair[i-1] + max(stair[i-2]+dp2[i-3], dp2[i-2])



print(dp2[N])
