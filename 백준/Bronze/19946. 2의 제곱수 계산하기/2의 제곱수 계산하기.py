N = int(input())
for i in range(64):
    tmp = 1
    for j in range(64):
        tmp*=2
        if i==j:
            tmp-=1
    if tmp==N:
        print(i+1)
        exit(0)
