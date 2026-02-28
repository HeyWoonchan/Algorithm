n = int(input())
p,q,r,s = map(int,input().split())
a = int(input())

arr = [0]*(2*n)
arr[1]=a
for i in range(1,n):
    arr[i*2] = arr[i]*p+q
    arr[i*2+1] = arr[i]*r+s

print(sum(arr[1:n+1]))