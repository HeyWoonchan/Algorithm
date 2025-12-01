import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
# print(arr)
ans = []
minAbsSum = 3e9
for i in range(N-2):
    for j in range(i+1, N-1):
        sum = arr[i]+arr[j]
        l = j+1;r = N-1
        while l<=r:
            mid = (l+r)//2
            tsum = sum+arr[mid]
            # print(arr[i],arr[j],arr[mid], "sum:",tsum)
            if abs(tsum)<minAbsSum:
                ans = [arr[i],arr[j],arr[mid]]
                minAbsSum = abs(tsum)
            if tsum<=0:
                l = mid+1
            else:
                r = mid-1

print(*ans)