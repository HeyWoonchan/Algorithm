arr=[]
num = [0]*(991)

for _ in range(10):
    a = int(input())
    num[a]+=1
    arr.append(a)

print(sum(arr)//10)
t = 0
ans = 0
for i in range(10,991,10):
    if num[i]>t:
        t = num[i]
        ans=i

print(ans)