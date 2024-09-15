answer = 0


def solution(numbers, target):
    global answer
    visited = [0]*len(numbers)
    def sol(n,numbers, arr, target):
        global answer
        if n==len(numbers):
            if sum(arr)==target:
                answer+=1
            # print(arr)
            return
        sol(n+1,numbers, arr+[numbers[n]],target)
        sol(n+1,numbers, arr+[-numbers[n]],target)
    sol(0,numbers,[],target)
    return answer