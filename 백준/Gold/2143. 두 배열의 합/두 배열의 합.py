T = int(input())
n = int(input())
nArr = list(map(int,input().split()))
m = int(input())
mArr = list(map(int,input().split()))

nSums = [0]*n
nSums[0]=nArr[0]
for i in range(1,n):
    nSums[i]=nSums[i-1]+nArr[i]
# print(nArr)
# print(nSums)

nSubSums = [[0]*n for _ in range(n)]
nSubSumsFloor = []
for i in range(n):
    for j in range(i,n):
        if i==0:
            nSubSums[i][j]=nSums[j]
            nSubSumsFloor.append(nSums[j])
            continue

        nSubSums[i][j]=nSums[j]-nSums[i-1]
        nSubSumsFloor.append(nSums[j]-nSums[i-1])
# print()
# print(*nSubSums,sep='\n')
# print(nSubSumsFloor)

mSums = [0]*m
mSums[0]=mArr[0]
for i in range(1,m):
    mSums[i]=mSums[i-1]+mArr[i]
# print(mArr)
# print(mSums)

mSubSums = [[0]*m for _ in range(m)]
mSubSumsFloor = []
for i in range(m):
    for j in range(i,m):
        if i==0:
            mSubSums[i][j]=mSums[j]
            mSubSumsFloor.append(mSums[j])
            continue
        mSubSums[i][j]=mSums[j]-mSums[i-1]
        mSubSumsFloor.append(mSums[j]-mSums[i-1])
# print()
# print(*mSubSums,sep='\n')
# print(mSubSumsFloor)

# print()
nSubSumsFloor.sort()
mSubSumsFloor.sort()


# print(nSubSumsFloor)
# print(mSubSumsFloor)
answer = 0
l=0;r=len(mSubSumsFloor)-1

while l<len(nSubSumsFloor) and r>=0:
    sum = nSubSumsFloor[l]+mSubSumsFloor[r]
    # print(nSubSumsFloor[l], mSubSumsFloor[r])
    if sum==T:
        # print("T==Sum",nSubSumsFloor[l], mSubSumsFloor[r])
        left = l+1;right = r-1
        while left<len(nSubSumsFloor) and nSubSumsFloor[l]==nSubSumsFloor[left]:
            left+=1
        while right>=0 and mSubSumsFloor[r]==mSubSumsFloor[right]:
            right -=1
        answer+=(left-l)*(r-right)
        l = left;r=right
    elif sum>T:
        r-=1
    else:
        l+=1
# print()

print(answer)
