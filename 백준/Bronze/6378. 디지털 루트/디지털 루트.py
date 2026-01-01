import sys
input=sys.stdin.readline

def dRoot(num):

    while num>=10:
        tNum=num
        t=0
        while tNum:
            t+=tNum%10
            tNum//=10
        num=t
    return num

while True:
    a = int(input())
    if a==0:
        break
    print(dRoot(a))
    