T, N = map(int,input().split())

for i in range(T):
    alphabet=[0]*26
    s = input()
    for j in s:
        alphabet[ord(j)-ord('a')]+=1
    firstHeavy=alphabet[ord(s[0])-ord('a')]

    FalseFlag=0
    for i in range(1,N):
        if firstHeavy>1:
            if i%2==1 and alphabet[ord(s[i])-ord('a')]>1:
                FalseFlag=1
                break
            if i%2==0 and alphabet[ord(s[i])-ord('a')]<=1:
                FalseFlag=1
                break
        else:
            if i%2==0 and alphabet[ord(s[i])-ord('a')]>1:
                FalseFlag=1
                break
            if i%2==1 and alphabet[ord(s[i])-ord('a')]<=1:
                FalseFlag=1
                break
    if FalseFlag==1:
        print("F")
    else:
        print("T")