c = 1000
def matmult(mat1, mat2):
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp+=mat1[i][k]*mat2[k][j]
            ans[i].append(tmp)
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            ans[i][j]%=c   
    return ans

def fastpow(mat,b):  
    if b==1:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]%=c 
        return mat
    #if b==0:
    #    return 1
    val = fastpow(mat,b//2)
    
    if b%2==1:
        result = matmult(matmult(val, val),mat)
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j]%=c 
        return result
    else:
        result = matmult(val, val)
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j]%=c 
        return result
    
N,B = map(int,input().split())
inMat = [list(map(int,input().split())) for _ in range(N)]
result = fastpow(inMat,B)
for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()