sudoku = [input() for _ in range(9)]
for i in range(9):
    temp = []
    for j in range(9):
        temp.append(ord(sudoku[i][j])-ord('0'))
    sudoku[i]=temp

# print(*sudoku, sep='\n')

def check(i,j,num):

    for x in range(9):
        if sudoku[i][x]==num:
            return False
        if sudoku[x][j]==num:
            return False
    # print("i,j:",i,j)
    row,col=-1,-1
    if 0<=i<3:
        row = 0
    elif 3<=i<6:
        row = 3
    else:
        row = 6

    if 0<=j<3:
        col = 0
    elif 3<=j<6:
        col = 3
    else:
        col = 6
    tcol = col
    for k in range(3):
        col=tcol
        for _ in range(3):
            # print("r,c:",row,col)
            if sudoku[row][col]==num:
                return False
            col+=1
        row+=1
    return True

def print_sol():
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end='')
        print()

def sol(depth):
    # print(depth)
    if depth==len(fills)-1:
        print_sol()
        exit(0)
        return
    
    nrow,ncol = fills[depth+1]
    for i in range(1,10):
        if check(nrow,ncol,i):
            # print("trying:",nrow,ncol,i)
            sudoku[nrow][ncol]=i
            sol(depth+1)
            sudoku[nrow][ncol]=0
    return



fills = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            fills.append((i,j))
fills_visited=[0]*len(fills)

# print("fills:", len(fills))


a,b = fills[0]
for i in range(1,10):
    if check(a,b,i):
        # print("trying:",a,b,i)
        sudoku[a][b]=i
        sol(0)
        sudoku[a][b]=0

