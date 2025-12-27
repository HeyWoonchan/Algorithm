while True:
    S = input()
    if S=="#":
        break

    a, b = S.split(' ',1)
    cnt=0
    for i in b:
        if i.lower()==a.lower():
            cnt+=1
    print(a,cnt)