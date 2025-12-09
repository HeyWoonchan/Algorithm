while True:
    year = int(input())
    if year==0:
        break

    f=True
    for y in range(1896, 2031,4):
        if y==year:
            if 1914<=y<=1918 or 1939<=y<=1945:
                print(y, "Games cancelled")
            
            elif y>2020:
                print(y, "No city yet chosen")
            else:
                print(y, "Summer Olympics")
            f = False
            break
    
    if f:
        print(year, "No summer games")
            