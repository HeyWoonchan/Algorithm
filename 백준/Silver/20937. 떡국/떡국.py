n = int(input())
arr=list(map(int,input().split()))
nums = [0]*50001
for a in arr:
    nums[a]+=1
ans=0
for a in nums:
    ans=max(ans,a)
print(ans)