import sys
input=sys.stdin.readline

N, M = map(int,input().split())
passwords={}
for _ in range(N):
    url, password = input().rstrip().split()
    passwords[url]=password
for _ in range(M):
    url=input().rstrip()
    print(passwords[url])