Mw,Mb = map(int,input().split())
Tw,Tb = map(int,input().split())
Pw,Pb = map(int,input().split())

w = min(Mb,Tw,Pb)
b = min(Mw,Tb,Pw)
if w==b:
    print(w*2)
else:
    print(min(w,b)*2+1)
    