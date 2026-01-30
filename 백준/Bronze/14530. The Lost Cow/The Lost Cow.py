firstx,y=map(int,input().split())
moving=1
totalMoved=0
right=True
x = firstx
if firstx==y:
    print(0)
    exit(0)
while True:
    # print("now length:",moving)
    while firstx-moving<x<firstx+moving:
        if right:
            x+=1
            totalMoved+=1
            if x==y:
                print(totalMoved)
                exit(0)
                break
            # if x==1001:
            #     x=1000
            #     break
        else:
            x-=1
            totalMoved+=1
            if x==y:
                print(totalMoved)
                exit(0)
                break
            # if x==-1:
            #     x=0
            #     break
             
        # print("now movi:",x)
    right = not right
    moving*=2

    