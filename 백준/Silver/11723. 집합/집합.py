import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    query = input().rstrip()
    if query=="all":
        S.clear()
        for i in range(20):
            S.add(i+1)
    elif query=="empty":
        S.clear()
    else:
        query, x = query.split()
        x = int(x)
        if query=="add":
            S.add(x)
        elif query=="remove":
            if x in S:
                S.remove(x)
        elif query=="check":
            if x in S:
                print(1)
            else:
                print(0)
        elif query=="toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)