remains=[0]*42
arr=[int(input()) for _ in range(10)]
for i in arr:
    remains[i%42]=1
print(sum(remains))