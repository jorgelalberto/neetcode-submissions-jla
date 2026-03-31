class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i in range(len(nums)):
            num = nums[i]
            if target-num in hashy:
                min_ind = min(hashy[target-num], i)
                max_ind = max(hashy[target-num], i)
                return [min_ind, max_ind]
            else:
                hashy[num] = i
        