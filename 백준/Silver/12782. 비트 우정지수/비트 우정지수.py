TC = int(input())
for _ in range(TC):
    a,b= input().split()
    #c:1에서 0으로 가야한느것
    #d:0에서 1로 가야하는것
    #min(c,d)+abs(c-d)
    c,d = 0,0

    for i in range(len(a)):
        if a[i]=='1' and b[i]=='0':
            c+=1
        elif a[i]=='0' and b[i]=='1':
            d+=1
    print(min(c,d)+abs(c-d))