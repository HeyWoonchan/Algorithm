#17140

r,c,k = map(int,input().split())

input_arr = [list(map(int,input().split())) for _ in range(3)]

max_r, max_c = 3,3
arr = [[0]*(100) for _ in range(100)]
for i in range(3):
    for j in range(3):
        arr[i][j] = input_arr[i][j]
time = 0

while time<=100:
    if max_r>=r and max_c>=c and arr[r-1][c-1]==k:
        break
    if max_r>=max_c: #행 정렬
        next_c = max_c
        for i in range(max_r):
            check = [0]*101
            tmp = []
            for j in range(max_c):
                check[arr[i][j]]+=1
            for j in range(1,101):
                if check[j]!=0:
                    tmp.append((j,check[j]))
            tmp.sort(key=lambda x: x[1])
            next_c = max(next_c, len(tmp)*2)
            if next_c>100:
                next_c=100
            put = []
            for iter in tmp:
                for z in [*iter]:
                    put.append(z)
            # print(put)
            arr[i] = [0]*100
            if len(put)<100:
                for j in range(len(put)):
                    arr[i][j] = put[j]
            else:
                for j in range(100):
                    arr[i][j] = put[j]
        # print(arr)
        max_c=next_c
    else:
        next_r = max_r
        for i in range(max_c):
            check = [0]*101
            tmp = []
            for j in range(max_r):
                check[arr[j][i]]+=1
            for j in range(1,101):
                if check[j]!=0:
                    tmp.append((j,check[j]))
            tmp.sort(key=lambda x: x[1])
            next_r = max(next_r, len(tmp)*2)
            if next_r>100:
                next_r=100
            put = []
            for iter in tmp:
                for z in [*iter]:
                    put.append(z)
            # print(put)
            for j in range(100):
                arr[j][i]=0
            if len(put)<100:
                for j in range(len(put)):
                    arr[j][i] = put[j]
            else:
                for j in range(100):
                    arr[j][i] = put[j]
        max_r=next_r
    time+=1

if time>100:
    print(-1)
else:
    print(time)


    
    