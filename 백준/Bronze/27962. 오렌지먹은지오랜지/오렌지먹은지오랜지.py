N=int(input())
S = input()

l=1
while l<=N:
    left=S[:l]
    right=S[N-l:]
    cnt=0
    for i in range(l):
        if left[i]!=right[i]:
            cnt+=1
    if cnt==1:
        print("YES")
        exit(0)
    l+=1
print('NO')