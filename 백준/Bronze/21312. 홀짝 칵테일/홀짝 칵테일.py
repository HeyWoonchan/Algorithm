A,B,C = map(int,input().split())
odds = []
evens = []

def isoddandappend(a,b):
    if (a*b)%2==1:
        odds.append(a*b)
    else:
        evens.append(a*b)
isoddandappend(A,1)
isoddandappend(B,1)
isoddandappend(C,1)
isoddandappend(A,B)
isoddandappend(A,C)
isoddandappend(B,C)
isoddandappend(A,B*C)

if len(odds)>0:
    print(max(odds))
else:
    print(max(evens))