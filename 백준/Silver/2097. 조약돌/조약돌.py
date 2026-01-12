N=int(input())
x=1;y=1
while True:
    if (x+1)*(y+1)>=N:
        break
    x+=1
    if (x+1)*(y+1)>=N:
        break
    y+=1
print(x+y+x+y)