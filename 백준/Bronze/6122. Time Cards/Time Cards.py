N, nlines = map(int,input().split())
starts = [0]*N
total = [0]*N
for _ in range(nlines):
    number, ss, hh,mm = input().split()
    number,hh,mm = map(int,(number,hh,mm))
    if ss=='START':
        starts[number-1]=hh*60+mm
    else:
        total[number-1]+=hh*60+mm-starts[number-1]
for i in range(N):
    print(total[i]//60, total[i]%60)