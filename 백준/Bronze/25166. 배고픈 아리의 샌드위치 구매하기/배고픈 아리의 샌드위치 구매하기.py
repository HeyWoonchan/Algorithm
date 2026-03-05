S, M = map(int,input().split())

ahriMoney = []
for i in range(10):
    ahriMoney.append(2**i)



# print(ahriMoney)



flag=0



st=[]
visited=[0]*10
def sol(c):
    if len(st)>10:
        return
    tsum = 0
    for i in st:
        tsum+=2**i
    if S==tsum:
        print("No thanks")
        exit(0)
    for i in range(c,10):
        if visited[i]==0:
            visited[i]=1
            st.append(i)
            sol(i+1)
            st.pop()
            visited[i]=0

st2=[]
visited2=[0]*10

poss = []

def sol2(c):
    if len(st2)>10:
        return
    tsum = 0
    for i in st2:
        tsum+=2**i
    if M==tsum:
        # print("쿠기구성",st2)
        for i in st2:
            poss.append(2**i)

    for i in range(c,10):
        if visited2[i]==0:
            visited2[i]=1
            st2.append(i)
            sol2(i+1)
            st2.pop()
            visited2[i]=0

st3 = []
visited3 = [0]*10
def sol3(rest,c):
    if len(st3)>len(poss):
        return
    tsum = 0
    for i in st3:
        tsum+=poss[i]
    if rest==tsum:
        print("Thanks")
        exit(0)
    for i in range(c,len(poss)):
        if visited3[i]==0:
            visited3[i]=1
            st3.append(i)
            sol3(rest,i+1)
            st3.pop()
            visited3[i]=0


if S<=1023:
    sol(0)
else:
    pass
    #남는돈을, M의 구성으로 완성 가능한가
    restMoney = S-1023
    #M의 구성 확인
    
    sol2(0)
    # print(poss)
    sol3(restMoney,0)
    print("Impossible")

    


