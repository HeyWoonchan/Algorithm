import sys
M = int(sys.stdin.readline())
s1 = set([])

for _ in range(M):
    cmdarr = list(sys.stdin.readline().split())
    if cmdarr[0]=='add':
        if int(cmdarr[1]) in s1:
            continue
        s1.add(int(cmdarr[1]))
    elif cmdarr[0]=='remove':
        if int(cmdarr[1]) not in s1:
            continue
        s1.remove(int(cmdarr[1]))
    elif cmdarr[0]=='check':
        if len(s1)==0:
            print(0)
            continue
        if int(cmdarr[1]) in s1:
            print(1)
        else:
            print(0)
    elif cmdarr[0]=='toggle':
        if len(s1)==0:
            s1.add(int(cmdarr[1]))
            continue
        if int(cmdarr[1]) in s1:
            s1.remove(int(cmdarr[1]))
        else:
            s1.add(int(cmdarr[1]))
    elif cmdarr[0]=='all':
        s1=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif cmdarr[0]=='empty':
        s1 = set([])