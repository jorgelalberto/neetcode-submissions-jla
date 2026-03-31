class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}

        for i, num in enumerate(nums):
            if target-num in hashy:
                return [min(i, hashy[target-num]), max(i, hashy[target-num])]
            hashy[num] = i
        
