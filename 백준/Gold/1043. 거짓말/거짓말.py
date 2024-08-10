N,M = map(int,input().split())

knows= input()
avoid_arr=set([])
if knows!="0":
    avoid_arr=set(list(map(int,knows.split()))[1:])

party_info_arr=[set(list(map(int,input().split()))[1:]) for _ in range(M)]

for _ in range(M):
    for j in range(M):
        party_info = party_info_arr[j]
        update_flag=False
        for i in party_info:
            if i in avoid_arr:
                update_flag=True
        if update_flag:
            for i in party_info:
                avoid_arr.add(i)
            
possible_num=0
for i in range(M):
    if party_info_arr[i].isdisjoint(avoid_arr):
        possible_num+=1

print(possible_num)