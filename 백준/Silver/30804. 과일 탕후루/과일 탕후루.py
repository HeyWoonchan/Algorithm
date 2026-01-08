N = int(input())
arr = list(map(int,input().split()))

result = 0


window = [0]*10
l=0
r=0
window[arr[l]]+=1
while 0<=l<N and 0<=r<N:
    
    check=0
    for i in range(10):
        if window[i]>0:
            check+=1
    # print(l,r,window, check)
    if check<=2:
        result = max(result,r-l+1)
        r+=1
        if r>=N:
            break
        window[arr[r]]+=1
    else:
        tmp = arr[l]
        window[arr[l]]-=1
        l+=1
        
print(result)

