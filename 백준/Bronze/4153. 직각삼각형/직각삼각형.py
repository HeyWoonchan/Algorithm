while True:
    a, b, c = map(int,input().split())
    if (a,b,c)==(0,0,0):
        break
    arr = [a,b,c]
    c = max(arr)
    t = 0
    for a in arr:
        if a!=c:
            t+=a*a
    if c*c==t:
        print("right")
    else:
        print("wrong")