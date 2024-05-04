N = int(input())

arr_1=[]
arr= [0]*(8003)
for _ in range(N):
    num = int(input())
    arr[num+4000]+=1
    arr_1.append(num)

arr_1.sort()

mid = arr_1[N//2]


many_1= 0

cnt_many = 0
for i in range(8003):
    if arr[i]>cnt_many:
        cnt_many = arr[i]

manyarr = []
for i in range(8003):
    if arr[i]==cnt_many:
        manyarr.append(i-4000)

if len(manyarr)>=2:
    many_1 = manyarr[1]
else:
    many_1 = manyarr[0]


avg = sum(arr_1)/N
# if avg>0:
#     if avg-int(avg)>=0.5:
#         avg = int(avg)+1
#     else:
#         avg = int(avg)
# else:
#     if avg+int(avg)<=-0.5:
#         avg = int(avg)-1
#     else:
#         avg = int(avg)
print(round(avg))
print(mid)
print(many_1)
print(arr_1[-1]-arr_1[0])