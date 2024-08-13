s = list(input());alpha = [0]*26
for i in s:
    alpha[ord(i)-ord('a')]+=1
print(*alpha,sep=' ')