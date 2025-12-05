import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []
AB= []
CD = []

#미리 AB, CD 더해놓고 탐색

for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a);B.append(b);C.append((c));D.append(d)

for i in range(n):
    for j in range(n):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])
AB.sort()
CD.sort()

answer = 0
l = 0;r = len(CD)-1
while l<len(AB) and r>=0:
    sum = AB[l]+CD[r]

    # print(sum)
   
    if sum==0:
        sameL = l+1
        while sameL<len(AB) and AB[l]==AB[sameL]:
            sameL+=1
        sameR = r-1
        while sameR>=0 and CD[r]==CD[sameR]:
            sameR-=1
        answer+= (sameL-l)*(r-sameR)
        r = sameR
        l = sameL
    
    elif sum>0:
        r-=1
    else:
        l+=1

                     
print(answer)