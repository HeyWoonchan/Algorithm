F=list(map(int,input().split()))
Frev = [0]*10
for i in range(10):
    Frev[F[i]]=i
Fa, Fb = input().split()
a = int("".join(str(Frev[int(s)]) for s in Fa))
b = int("".join(str(Frev[int(s)]) for s in Fb))
Fab = "".join(str(F[int(s)]) for s in str(a+b))
print(Fab)