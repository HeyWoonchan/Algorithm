N = int(input())
solutions = list(map(int,input().split()))
MAXNUM = 1000000000*3


i, j =0,1
answer = []
if solutions[0]<0 and solutions[-1]>0:
    while not (solutions[i]<0 and solutions[j]>0):
        i+=1
        j+=1
    nowSum = 0
    nowMinAbs = MAXNUM
    while N>i>=0 and 0<=j<N:
        nowSum = solutions[i]+solutions[j]
        if abs(nowSum)<nowMinAbs:
            nowMinAbs = abs(nowSum)
            answer = [solutions[i],solutions[j]]

        left= abs(solutions[i-1]+solutions[j]) if i-1>=0 else MAXNUM
        right= abs(solutions[i]+solutions[j+1]) if j+1<N else MAXNUM
        if left<=right:
            i-=1
        else:
            j+=1
    i=0;j=1
    while j+1<N and not solutions[j+1]>0:
        i+=1
        j+=1
    nowSum = 0
    nowMinAbs = MAXNUM
    while N>i>=0 and 0<=j<N:
        nowSum = solutions[i]+solutions[j]
        if abs(nowSum)<nowMinAbs:
            nowMinAbs = abs(nowSum)
            answer = [solutions[i],solutions[j]]

        left= abs(solutions[i-1]+solutions[j]) if i-1>=0 else MAXNUM
        right= abs(solutions[i]+solutions[j+1]) if j+1<N else MAXNUM
        if left<=right:
            i-=1
        else:
            j+=1
    i=0;j=1
    while j+2<N and  not solutions[i]>0:
        i+=1
        j+=1
    nowSum = 0
    nowMinAbs = MAXNUM
    while N>i>=0 and 0<=j<N:
        nowSum = solutions[i]+solutions[j]
        if abs(nowSum)<nowMinAbs:
            nowMinAbs = abs(nowSum)
            answer = [solutions[i],solutions[j]]

        left= abs(solutions[i-1]+solutions[j]) if i-1>=0 else MAXNUM
        right= abs(solutions[i]+solutions[j+1]) if j+1<N else MAXNUM
        if left<=right:
            i-=1
        else:
            j+=1





elif solutions[0]<0 and solutions[-1]<0:
    answer = [solutions[-2], solutions[-1]]
elif solutions[0]>0:
    answer = [solutions[0], solutions[1]]




print(*answer, sep=' ')