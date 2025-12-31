import sys
input=sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    age, name = input().strip().split()
    age=int(age)
    arr.append((age,i,name))
arr.sort()
for age,i,name in arr:
    print(age,name)