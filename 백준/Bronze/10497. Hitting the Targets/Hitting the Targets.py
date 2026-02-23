m = int(input())
circles = []
rectangles = []
for _ in range(m):
    inn = list(input().split())
    if inn[0]=='rectangle':
        rectangles.append(tuple(map(int,inn[1:])))
    else:
        circles.append(tuple(map(int,inn[1:])))
n = int(input())
for _ in range(n):
    ans = 0
    x,y=map(int,input().split())
    for x1,y1,x2,y2 in rectangles:
        if x1<=x<=x2 and y1<=y<=y2:
            ans+=1
    for x1,y1,r in circles:
        if (x-x1)**2+(y-y1)**2<=r**2:
            ans+=1
    print(ans)