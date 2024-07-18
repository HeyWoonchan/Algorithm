T = int(input())

for _ in range(T):
    forward = 1
    startidx = 0
    
    errorflag = False

    command = list(input())
    arr_len = int(input())

    endidx = arr_len
    if arr_len==0:
        _=input()
        arr_str=[]
    else:
        arr_str = list(map(int,input()[1:-1].split(',')))
    for com in command:
        if com=="R":
            forward = not forward
        elif com=="D":
            if startidx==endidx:
                errorflag=True
                continue
            if forward:
                startidx+=1
            else:
                endidx-=1
    if errorflag:
        print("error")
        continue
    if forward:
        print('[',end='')
        print(*arr_str[startidx:endidx],sep=',',end=']')
        print()
    else:
        print('[',end='')
        print(*arr_str[startidx:endidx][::-1],sep=',',end=']')
        print()    