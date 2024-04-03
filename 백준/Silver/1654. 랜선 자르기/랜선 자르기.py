# 랜선 자르기

K, N= map(int, input().split())



"""


11개를 만들기 위한 랜선의 최대 길이




"""

arr=list(int(input()) for _ in range(K))

# arr.sort()

# initial = sum(arr) //N


# # bruteforce
# while 1:
#     sum = 0
#     for i in range(len(arr)):
#         sum+= arr[i]//initial
    
#     if sum == N:
#         break
#     else:
#         initial -=1
    


    

# binary search

first = 1
last = 2147483647
answer=0
while first <=last:
    mid = (first + last) // 2
    
    # print(first, last,mid)
    sum = 0
    flag = True
    for i in range(len(arr)):
        sum+= arr[i]//mid
    if sum>=N:
        # print("N개보다 많이 나옴, 높여서 진행")
        first = mid+1
        answer = mid
    else:
        # print("N보다 적음 낮춰서 진행")
        last = mid-1

# #check 


#dp?

      

print(last)
