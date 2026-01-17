t=int(input())
for _ in range(t):
    a=input()
    b=input()
    flag=True
    for s in b:
        if s not in a:
            flag=False
            break
    if flag==True:
        print("YES")
    else:
        print("NO")