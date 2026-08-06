class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i, num in enumerate(nums):
            j = hashy.get(target-num, False)
            if type(j) is int:
                return [j, i]
            hashy[num] = i