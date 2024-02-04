class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            i_val = nums[i]
            if i == j:
                break
            for j in range(1,len(nums)):
                j_val = nums[j]
                if i_val + j_val == target:
                    output.append(i)
                    output.append(j)
                    return output
"""



