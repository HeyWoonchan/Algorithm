from collections import deque
n = int(input())

suggested = [0]*n

for i in range(n):
    suggested[i]=int(input())


suggested.sort()

# print(suggested)




limit = (n*15)/100
if limit-int(limit)>=0.5:
    limit = int(limit)+1
else:
    limit = int(limit)
# print(limit)
# print((n*15)/100)

if limit != 0:
    suggested = deque(suggested)
    for _ in range(limit):
        suggested.pop()
        suggested.popleft()


# print(suggested)
if n==0:
    print(0)
else:
    if len(suggested)==0:
        print(0)
    else:
        avg = sum(suggested)/len(suggested)
        if avg-int(avg)>=0.5:
            avg = int(avg)+1
        else:
            avg = int(avg)
        print(avg)
        
