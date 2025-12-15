import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

oddstart = []
evenstart = []
oddflag = 0
evenflag = 0
for a in arr:
    if oddflag==0 and a%2==1:
        oddstart.append(a)
        oddflag=1
    elif oddflag==1 and a%2==0:
        oddstart.append(a)
        oddflag=0
    if evenflag==0 and a%2==0:
        evenstart.append(a)
        evenflag=1
    elif evenflag==1 and a%2==1:
        evenstart.append(a)
        evenflag=0

print(max(len(evenstart),len(oddstart)))