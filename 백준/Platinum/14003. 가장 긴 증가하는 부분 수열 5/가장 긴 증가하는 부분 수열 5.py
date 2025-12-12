import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

tails = [0]*(N+1) #tails[k] : 길이가 k+1인 증가 부분 수열의 마지막값(최댓값)
tails[0]=arr[0]
nowMaxIndex = 0

def findindexL(n, R):
    l, r = 0,R
    
    while l<=r:
        mid = (l+r)//2
        if tails[mid]>=n:
            r=mid-1
        else:
            l=mid+1
    return l

lastindexs = [-1]*(N+1)
lastNumIndexes = [-1]*(N+1)
nowNumIndexes = [-1]*(N+1)
nowNumIndexes[0]=0

# print()
# print("now tails:", tails)
# print("now lni:", lastNumIndexes)
# print("now nni:", nowNumIndexes)

for i, num in enumerate(arr):
    if i==0:
        continue
    # print(i)
    # print("now num:", num)
    
    if tails[nowMaxIndex]<num: #가장 긴 증가 수열의 마지막값보다 현재 탐색값이 더 크면, 바로 새로운 길이로 갱신
        # print("마지막 tail값보다 큼")
        # lastNums[num]=tails[nowMaxIndex]
        
        nowMaxIndex+=1
        tails[nowMaxIndex]=num
        nowNumIndexes[nowMaxIndex]=i
        lastNumIndexes[i] = nowNumIndexes[nowMaxIndex-1]
        #어디서 넘어온 것인가를 계속 담으면 마지막에 역추적 가능?
        
        
    else: 
        t = findindexL(num, nowMaxIndex)
        # print("사이값임, t:",t)
        # if tails[t]>num:
        
        if tails[t]>num: #tails[t] in lastNums: #dict 사용하면 시간초과
            # lastNums[num] = lastNums[tails[t]] 
            lastNumIndexes[i] = nowNumIndexes[t-1]
            nowNumIndexes[t]=i
        tails[t] = num
    # print("now tails:", tails)
    # print("now lni:", lastNumIndexes)
    # print("now nni:", nowNumIndexes)


print(nowMaxIndex+1)
# print(tails)


# print(lastNumIndexes)

#각 숫자별로, 어느 숫자에서 넘어온 것인지 알아내면 된다.
#중간에 바뀌면, 어차피 나중에 또 그 값에서 바뀌어서 올라옴.
answer = []
# if tails[nowMaxIndex] in lastNums :
#     t = tails[nowMaxIndex]
# else:
#     t = ''
# while True:
#     if t=='':
#         break
#     answer.append(t)
#     if t in lastNums:
#         t = lastNums[t]
#     else:
#         t = ''
t = nowNumIndexes[nowMaxIndex]
while t!=-1:
    answer.append(arr[t])
    t = lastNumIndexes[t]
print(*answer[::-1])



