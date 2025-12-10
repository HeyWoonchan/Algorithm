import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
S = [0]


def findIndex(num):
    l,r = 0,len(S)-1
    while l<=r:
        mid = (l+r)//2
        if S[mid]>=num:
            r=mid-1
        else:
            l=mid+1
    return l

for i in range(N):
    # print(S)
    if A[i]>S[-1]:
        S.append(A[i])
    elif A[i]<S[-1]:
        index = findIndex(A[i])
        if S[index]>A[i]:
            S[index]=A[i]

print(len(S)-1)