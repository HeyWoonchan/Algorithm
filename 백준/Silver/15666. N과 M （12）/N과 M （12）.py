#15666

N, M = map(int,input().split())

inarr = list(map(int,input().split()))
inarr.sort()
result = []
def sol(arr,c):

    if len(arr)==M:
        result.append(tuple(arr))
        return
    
    for i in range(c,len(inarr)):
        sol(arr+[inarr[i]],i)

sol([],0)
result = list(set(result))
result.sort()
for i in result:
    print(*i, sep=' ')