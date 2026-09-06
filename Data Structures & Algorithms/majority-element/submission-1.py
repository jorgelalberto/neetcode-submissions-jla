class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEle = nums[0]
        cnt = 1
        for num in nums:
            if num == majEle:
                cnt += 1
            elif num != majEle and cnt > 0:
                cnt -= 1
            elif num != majEle and cnt == 0:
                majEle = num
                cnt += 1
        return majEle