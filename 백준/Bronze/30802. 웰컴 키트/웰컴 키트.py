N = int(input())
arr = list(map(int,input().split()))
T, P = map(int,input().split())
tShirt= 0
for a in arr:
    tShirt+=(a-1)//T+1
print(tShirt)
print(N//P,N%P)