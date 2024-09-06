# 부분수열을 둘 다 모두 뽑고
# 공통인 것을 추린다?
# 가장 큰 공통 숫자를 뽑고 그뒤로 최대공통수열 하기 ㅇㅇ

N = int(input())
arrA = list(map(int,input().split()))
M = int(input())
arrB = list(map(int,input().split()))

result = []
def sol(arr1, arr2):
    if len(arr1)==0 or len(arr2)==0:
        return
    idxs = [[] for _ in range(101)]
    for i in range(len(arr1)):
        idxs[arr1[i]].append(i)

    common_max = 0
    idx1=0
    idx2 = 0
    for i in range(len(arr2)):
        if len(idxs[arr2[i]])>0 and common_max<arr2[i]:
            common_max = arr2[i]
            idx1 = idxs[arr2[i]][0]
            idx2 = i
    
    if common_max==0:
        return
    result.append(common_max)

    nextarr1_start = idx1+1
    nextarr2_start = idx2+1

    if nextarr1_start>=len(arr1) or nextarr2_start>=len(arr2):
        return
    sol(arr1[nextarr1_start:], arr2[nextarr2_start:])  
        
sol(arrA,arrB)

if len(result)!=0:
    print(len(result))
    print(*result)
else:
    print(0)