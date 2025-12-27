N = int(input())


for i in range(1,N):
    t=i
    t2=i
    while t2:
        t+=t2%10
        t2//=10
    if t==N:
        print(i)  
        exit(0)
print(0)