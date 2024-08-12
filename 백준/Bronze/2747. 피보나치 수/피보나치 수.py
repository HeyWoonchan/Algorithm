f,s = 0,1
tmp=0
n = int(input())
for i in range(n):
    tmp = f+s
    f,s = s,tmp
print(f)