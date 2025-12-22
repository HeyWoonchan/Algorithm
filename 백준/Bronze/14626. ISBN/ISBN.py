isbn = input()
m = int(isbn[-1])
mul = [1,3,1,3,1,3,1,3,1,3,1,3]
lsum = 0
si = 0
for i in range(12):
    if isbn[i]=='*':
        si=i
        continue
    lsum+=int(isbn[i])*mul[i]
for i in range(10):
    if (lsum+i*mul[si]+m)%10==0:
        print(i)
        exit(0)