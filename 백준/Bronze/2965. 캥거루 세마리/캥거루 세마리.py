a,b,c = map(int,input().split())

move =0
while not (a+1==b and a+2==c):
    ab = b-a
    bc = c-b
    if ab<bc:
        a,b = b,b+1
    else:
        b,c = b-1,b
    move+=1
    # print(a,b,c)

print(move)