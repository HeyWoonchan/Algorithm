def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

N = int(input())
cnt=0
board = N
while board>1:
    flag = 0
    for i in range(2,board):
        if gcd(board,i)==1:
            cnt+=1
            board=i
            flag=1
            break
    if flag==0:
        break
print("Song" if cnt%2==0 else "Soomin")