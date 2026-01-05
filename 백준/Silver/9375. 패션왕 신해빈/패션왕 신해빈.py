TC = int(input())
for _ in range(TC):
    n = int(input())
    clothes = {}
    for i in range(n):
        _, tp= input().split()
        if tp not in clothes:
            clothes[tp]=1
        else:
            clothes[tp]+=1
    ans=1
    for a in clothes.keys():
        ans*=(clothes[a]+1)
    print(ans-1)