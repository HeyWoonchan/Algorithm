def find(whole ,page):
    for i in range(1,whole//2+1,2):
        arr = [i,i+1,whole-1-i+1,whole-i+1]
        if page in arr:
            for a in arr:
                if page!=a:
                    print(a,end=' ')
            print()
            return

while True:
    q = input()
    if q=='0':
        break
    N, P = map(int,q.split())
    find(N,P)

