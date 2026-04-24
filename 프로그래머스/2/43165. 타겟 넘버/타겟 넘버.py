def solution(numbers, target):
    def sol(depth, nowSum):
        if depth>len(numbers):
            return 0
        if depth==len(numbers) and nowSum==target:
            return 1
        # print(depth, nowSum)
        ans=0
        if depth<len(numbers):
            ans+=sol(depth+1, nowSum+numbers[depth])
            ans+=sol(depth+1, nowSum-numbers[depth])
        return ans
    answer = sol(0,0)
    return answer