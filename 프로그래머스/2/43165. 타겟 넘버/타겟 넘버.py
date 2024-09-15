


def solution(numbers, target):
    def sol(n,numbers, tmp, target):
        answer=0
        if n==len(numbers):
            if tmp==target:
                answer+=1
            # print(arr)
            return answer
        answer+=sol(n+1,numbers, tmp+numbers[n],target)
        answer+=sol(n+1,numbers, tmp-numbers[n],target)
        return answer
    
    answer=sol(0,numbers,0,target)
    return answer