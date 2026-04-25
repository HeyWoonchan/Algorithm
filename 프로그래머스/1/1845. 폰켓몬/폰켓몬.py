def solution(nums):
    
    #N마리 중 N/2마리 가져가기
    #N/2마리를 고르는데, 가장 많은 종류의 폰켓몬을 선택하는 방법
    types = len(set(nums))
    N = len(nums)
    if types>=N//2:
        return N//2
    else:
        return types
    
