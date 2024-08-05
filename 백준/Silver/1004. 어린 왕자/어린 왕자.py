T = int(input())

for _ in range(T):
    x1,y1, x2,y2 = map(int,input().split())
    n = int(input())
    planets = [tuple(map(int, input().split())) for _ in range(n)]

    result = 0
    for cx, cy, r in planets:
        
        dist1 = (x1-cx)**2+(y1-cy)**2

        dist2 = (x2-cx)**2+(y2-cy)**2

        rr = r**2
        if dist1<rr and dist2<rr:
            continue
        if dist1<rr:
            result+=1
        if dist2<rr:
            result+=1

    print(result)