arr = open(0)
for a in arr:
    a,b = map(int,a.rstrip().split())
    print(b//(a+1))