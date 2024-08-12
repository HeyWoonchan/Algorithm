f,s = 0,1
n = int(input())
for i in range(n):
    f,s = s, f+s
print(f)