A=input()
B=input()
ans=[]
ans.append(abs(ord(A[0])-ord(B[0])))
ans.append(abs(int(A[1])-int(B[1])))
ans.sort()
print(*ans)