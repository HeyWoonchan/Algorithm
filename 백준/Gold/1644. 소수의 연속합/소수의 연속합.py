N = int(input())
if N==1:
    print(0)
    exit(0)


numbers = [True]*(N+1)
numbers[0],numbers[1]=False,False
for i in range(2,N+1):
    if numbers[i]==False:
        continue
    for j in range(2*i,N+1,i):
        numbers[j]=False


primes = []
for i in range(1,N+1):
    if numbers[i]:
        primes.append(i)

i,j = 0,0
nowSum = primes[0]
# print(len(primes))
answer = 0
while True:
    # print("i,j",i,j)
    if nowSum<=N:
        if nowSum==N:
            answer+=1
        j+=1
        if j>=len(primes):
            break
        nowSum+=primes[j]
    else:
        nowSum-=primes[i]
        i+=1
        if i>=len(primes):
            break
    
    
print(answer)
    
    