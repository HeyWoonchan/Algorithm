A, B , C = map(int,input().split())


def sol(a,b,c):  
    if b==1:
        return a%c
    if b==0:
        return 1
    val = sol(a,b//2,c)

    if b%2==1:
        return (val*val*a)%c
    else:
        return (val*val)%c


print(sol(A,B,C))