arr = list(map(int,input().split()))
t = 0
for i in arr:
    t+=i*i
print(t%10)