# def per(L,O,V,E):
#     return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) * 100

# yL,yO,yV,yE=0,0,0,0
# yeondo=input()
# for s in yeondo:
#     if s=='L':
#         yL+=1
#     elif s=='O':
#         yO+=1
#     elif s=='V':
#         yV+=1
#     elif s=='E':
#         yE+=1

# N=int(input())

# nowMax = -1
# ans=chr(ord('Z')+1)
# sArr=[input() for _ in range(N)]
# for i in range(N):
#     tL,tO,tV,tE=0,0,0,0
#     S = sArr[i]
#     for s in S:
#         if s=='L':
#             tL+=1
#         elif s=='O':
#             tO+=1
#         elif s=='V':
#             tV+=1
#         elif s=='E':
#             tE+=1
#     p = per(yL+tL, yO+tO,yV+tV,yE+tE)
#     if nowMax<= p:
#         if nowMax==p:
#             if ans>S:
#                 ans=S
#         else:
#             nowMax=p
#             ans=S
# if nowMax==-1:
#     print(sorted(sArr)[0])
# else:
#     print(ans)


yeondo=input()
N=int(input())
nowMax=0
ans=chr(ord('Z')+1)
L=0;O=0;V=0;E=0
for s in yeondo:
    if s=='L':
        L+=1
    elif s=='O':
        O+=1
    elif s=='V':
        V+=1
    elif s=='E':
        E+=1

def per(L,O,V,E):
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
sArr=[input() for _ in range(N)]
for i in range(N):
    tL,tO,tV,tE=0,0,0,0
    S=sArr[i]
    for s in S:
        if s=='L':
            tL+=1
        elif s=='O':
            tO+=1
        elif s=='V':
            tV+=1
        elif s=='E':
            tE+=1
    p = per(L+tL, O+tO, V+tV,E+ tE)
    if nowMax<=p:
        if nowMax<p:

            nowMax=p
            ans=S
        elif nowMax==p and ans>=S:
            ans=S

if nowMax==0:
    print(sorted(sArr)[0])
else:
    print(ans)
    