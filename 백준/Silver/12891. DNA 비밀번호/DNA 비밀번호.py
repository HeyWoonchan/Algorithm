S, P = map(int,input().split())
DNA = list(input())
A,C,G,T = map(int,input().split())

left, right = 0, P-1

now = [0]*4
cnt = 0
def slide_right(added):
    # print(now)
    if added=='A':
        now[0]+=1
    elif added=='C':
        now[1]+=1
    elif added=='G':
        now[2]+=1
    elif added=='T':
        now[3]+=1

def slide_left(subbed):
    # print(now)
    if subbed=='A':
        now[0]-=1
    elif subbed=='C':
        now[1]-=1
    elif subbed=='G':
        now[2]-=1
    elif subbed=='T':
        now[3]-=1

for i in range(left, P):
    slide_right(DNA[i])

while True:
    # print(right)
    if now[0]>=A and now[1]>=C and now[2]>=G and now[3]>=T:
        cnt+=1
    if right>=S-1:
        break

    right+=1
    
    slide_right(DNA[right])
    slide_left(DNA[left])
    left+=1

print(cnt)