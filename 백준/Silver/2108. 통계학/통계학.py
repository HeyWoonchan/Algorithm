import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

print(round(sum(arr)/N))
arr.sort()
print(arr[(N)//2])
count = [0]*(8002)
for a in arr:
    count[a]+=1
manyArr = []
manyAns = max(count)
for i in range(-4000,4001):
    if manyAns==count[i]:
        manyArr.append(i)
manyArr.sort()
if len(manyArr)>1:
    print(manyArr[1])
else:
    print(manyArr[0])
# print(manyArr)
print(arr[-1]-arr[0])        
