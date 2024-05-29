N = int(input())
M = int(input())
bButtons=[]
if M>0:
    bButtons=list(map(int, input().split()))
nowChannel=100
"""
    +버튼, 번호입력, 이전번호까지 온 후 +버튼
100 - 0, 3 
101 - 1, 3, 1
102 - 2, 3
103 - 3, 3
104 - 4, 3
105 - 5, 3
+버튼으로 가능경우 or 숫자버튼에다가 +버튼
"""
arr = [0]*1000001

# 채널이 100이상인경우
for i in range(100, 1000000):
    if i==100:
        arr[i]=0
    else:
        typing = 0
        dial = i
        while dial>0:
            # print(dial)
            if dial%10 in bButtons:
                typing = 1e9
                break
            else:
                dial//=10
                typing+=1
        before_plus = arr[i-1]+1
        arr[i] = min(before_plus, typing)


for i in range(99,0,-1):
    typing = 0
    dial = i
      
    while dial>0:
        # print(dial)
        if dial%10 in bButtons:
            typing = 1e9
            break
        else:
            dial//=10
            typing+=1
    arr[i]=min(arr[i+1]+1, typing)

if 0 in bButtons:
    arr[0] = arr[1]+1
else:
    arr[0] = 1

# print(arr[:101])

for i in range(1,100):
    arr[i] = min(arr[i], arr[i-1]+1)

#다시 내려오면서, 올라가면서 했던 최솟값 vs 이전값

for i in range(999999,99,-1):
    arr[i] = min(arr[i], arr[i+1]+1)

# print(arr[:101])

print(arr[N])