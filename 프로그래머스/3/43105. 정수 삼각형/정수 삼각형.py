def solution(triangle):
    answer = 0
    
    for i in range(1,len(triangle)):
        triangle[i][0]+=triangle[i-1][0]
        for j in range(1,len(triangle[i])-1):
            triangle[i][j]=triangle[i][j]+max(triangle[i-1][j-1],triangle[i-1][j])
        triangle[i][-1] +=triangle[i-1][-1]
    return max(triangle[-1])