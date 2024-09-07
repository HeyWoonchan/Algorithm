M = int(input())

rest = 1000000007

result = 0
for _ in range(M):
    n, s = map(int,input().split())
    tmp = pow(n,rest-2,rest)
    result += pow(tmp*s, 1,rest)

print(result%rest)

