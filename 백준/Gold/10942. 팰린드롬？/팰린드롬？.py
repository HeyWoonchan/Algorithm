import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

# def ispelindrome(string,i):
#     if len(string)==1:
#         return 1
#     if len(string)//2==i:
#         return 1
#     if string[i]!=string[len(string)-1-i]:
#         return 0
#     return ispelindrome(string,i+1)

# string = "1234554321"

def ispelindromeDP(target,i,j):
    if i>=j:
        return 1
    if target[i]!=target[j]:
        return 0
    if dp[i+1][j-1]==-1:
        answer =  ispelindromeDP(target, i+1,j-1)
        dp[i+1][j-1]=answer
    else:
        answer = dp[i+1][j-1]
    return answer

# print(ispelindromeDP(string,0,len(string)-1))

N = int(input())
number = list(map(int,input().split()))
M = int(input())
queries = []

for _ in range(M):
    S, E = map(int,input().split())
    queries.append((S-1,E-1))

dp = [[-1]*N for _ in range(N)]

for i in range(N):
    for j in range(N-1,-1,-1):
        if dp[i][j]!=-1:
            continue
        ans = ispelindromeDP(number,i,j)
        if ans==1:
            dp[i][j]=1
        else:
            dp[i][j]=0
    

for s, e in queries:
    print(dp[s][e])
