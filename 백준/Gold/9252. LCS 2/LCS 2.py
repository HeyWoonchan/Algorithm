first = input().rstrip()
second = input().rstrip()

dp=[[0]*(len(second)+1) for _ in range(len(first)+1)]
dp2=[[('',-1,-1)]*(len(second)+1) for _ in range(len(first)+1)]

nowmax = 0
ans = []
for i in range(1,len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1]==second[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            if dp[i][j]>nowmax:
                nowmax = dp[i][j]
            dp2[i][j]=(first[i-1],i-1,j-1)
            
        else:
            if dp[i][j-1]>dp[i-1][j]:
                dp2[i][j]=dp2[i][j-1]
            else:
                dp2[i][j]=dp2[i-1][j]
            dp[i][j]=max(dp[i][j-1], dp[i-1][j])
print(nowmax)  

r,c = -1,-1
for i in range(1,len(first)+1):
    flag= 0
    for j in range(1, len(second)+1):
        if dp[i][j]==nowmax:
            r=i
            c=j
            flag = 1
            break
    if flag==1:
        break
# print(*dp2, sep='\n')
while (r,c)!=(-1,-1):
      
    A, r,c = dp2[r][c]
    ans.append(A)  

# print()
# print(*dp, sep='\n')
    
if nowmax!=0:    
    print(''.join(ans[::-1]))
