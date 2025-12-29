N = int(input())
alpha = [0]*26
for _ in range(N):
    S1, S2 = input().split()
    t = [0]*26
    for a in S1:
        t[ord(a)-ord('a')]+=1
    t2 = [0]*26
    for a in S2:
        t2[ord(a)-ord('a')]+=1
    for i in range(26):
        alpha[i]+=max(t[i],t2[i])
        
print(*alpha, sep='\n')