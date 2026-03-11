TC = int(input())

cube = [[['w','w','w'],
         ['w','w','w'],
         ['w','w','w']],
         [['r','r','r'],
         ['r','r','r'],
         ['r','r','r']],
         [['y','y','y'],
         ['y','y','y'],
         ['y','y','y']],
         [['o','o','o'],
         ['o','o','o'],
         ['o','o','o']],
         [['b','b','b'],
         ['b','b','b'],
         ['b','b','b']],
         [['g','g','g'],
         ['g','g','g'],
         ['g','g','g']],]

def init():
    global cube
    cube = [[['w','w','w'],
         ['w','w','w'],
         ['w','w','w']],
         [['r','r','r'],
         ['r','r','r'],
         ['r','r','r']],
         [['y','y','y'],
         ['y','y','y'],
         ['y','y','y']],
         [['o','o','o'],
         ['o','o','o'],
         ['o','o','o']],
         [['b','b','b'],
         ['b','b','b'],
         ['b','b','b']],
         [['g','g','g'],
         ['g','g','g'],
         ['g','g','g']],]

def rotateArr90(arr):
    arr = list(map(list,zip(*arr[::-1])))
    return arr

def rotateU(clockwise: str):
    if clockwise=='+':
        cube[0]=rotateArr90(cube[0])
        cube[5][0],cube[3][0],cube[4][0],cube[1][0]=cube[1][0],cube[5][0],cube[3][0],cube[4][0]
    else:
        for _ in range(3):
            rotateU('+')   
    return

def rotateD(clockwise: str):
    if clockwise=='-':
        for _ in range(3):
            cube[2]=rotateArr90(cube[2])
        cube[5][2],cube[3][2],cube[4][2],cube[1][2]=cube[1][2],cube[5][2],cube[3][2],cube[4][2]
    else:
        for _ in range(3):
            rotateD('-')
    return

def rotateF(clockwise: str):
    if clockwise=='+':
        cube[1]=rotateArr90(cube[1])
        cube[0][2][0],cube[0][2][1],cube[0][2][2],cube[4][0][0],cube[4][1][0],cube[4][2][0],cube[2][0][2],cube[2][0][1],cube[2][0][0],cube[5][2][2],cube[5][1][2],cube[5][0][2]=cube[5][2][2],cube[5][1][2],cube[5][0][2],cube[0][2][0],cube[0][2][1],cube[0][2][2],cube[4][0][0],cube[4][1][0],cube[4][2][0],cube[2][0][2],cube[2][0][1],cube[2][0][0]
    else:
        for _ in range(3):
            rotateF('+')
    return
def rotateB(clockwise: str):
    if clockwise=='+':
        cube[3]=rotateArr90(cube[3])
        cube[0][0][2],cube[0][0][1],cube[0][0][0],cube[5][0][0],cube[5][1][0],cube[5][2][0],cube[2][2][0],cube[2][2][1],cube[2][2][2],cube[4][2][2],cube[4][1][2],cube[4][0][2]=cube[4][2][2],cube[4][1][2],cube[4][0][2],cube[0][0][2],cube[0][0][1],cube[0][0][0],cube[5][0][0],cube[5][1][0],cube[5][2][0],cube[2][2][0],cube[2][2][1],cube[2][2][2]
    else:
        for _ in range(3):
            rotateB('+')
    return
def rotateL(clockwise: str):
    if clockwise=='+':
        cube[5] =rotateArr90(cube[5])
        cube[0][0][0],cube[0][1][0],cube[0][2][0],cube[1][0][0],cube[1][1][0],cube[1][2][0],cube[2][0][0],cube[2][1][0],cube[2][2][0],cube[3][2][2],cube[3][1][2],cube[3][0][2]=cube[3][2][2],cube[3][1][2],cube[3][0][2],cube[0][0][0],cube[0][1][0],cube[0][2][0],cube[1][0][0],cube[1][1][0],cube[1][2][0],cube[2][0][0],cube[2][1][0],cube[2][2][0]
    else:
        for _ in range(3):
            rotateL('+')
    return
def rotateR(clockwise: str):
    if clockwise=='+':
        cube[4]=rotateArr90(cube[4])
        cube[0][2][2],cube[0][1][2],cube[0][0][2],cube[3][0][0],cube[3][1][0],cube[3][2][0],cube[2][2][2],cube[2][1][2],cube[2][0][2],cube[1][2][2],cube[1][1][2],cube[1][0][2]=cube[1][2][2],cube[1][1][2],cube[1][0][2],cube[0][2][2],cube[0][1][2],cube[0][0][2],cube[3][0][0],cube[3][1][0],cube[3][2][0],cube[2][2][2],cube[2][1][2],cube[2][0][2]
    else:
        for _ in range(3):
            rotateR('+')
    return

def rotate(where: str, clockwise: str):
    if where=='U':
        rotateU(clockwise)
    elif where=='D':
        rotateD(clockwise)
    elif where=='F':
        rotateF(clockwise)
    elif where=='B':
        rotateB(clockwise)
    elif where=='L':
        rotateL(clockwise)
    elif where=='R':
        rotateR(clockwise)

for _ in range(TC):
    init()
    n = int(input())
    inputStr = input()
    for i in range(0,n*2+n-1,3):
        rotate(inputStr[i],inputStr[i+1])
    for i in range(3):
        print(''.join(cube[0][i]))






