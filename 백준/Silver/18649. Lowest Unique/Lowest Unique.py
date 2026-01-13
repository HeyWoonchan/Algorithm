import sys
n,k,m=map(int,sys.stdin.readline().split())
for _ in range(m):
    for i in range(1,k+1):
        sys.stdout.write(str(i)+' ')
    sys.stdout.write('\n')
    input()
    