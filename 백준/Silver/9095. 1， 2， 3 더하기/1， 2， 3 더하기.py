T = int(input())

tests = [int(input()) for _ in range(T)]

# 1만 뽑는 경우
# 2만 뽑는 경우
# 3만 뽑는 경우
# 1,2
# 1,3
# 2,3
# 1,2,3

arr = [0]*11

arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4,11):
    arr[i] = arr[i-1]+arr[i-2]+arr[i-3]

for test in tests:
    print(arr[test])
    
    
    

