class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_num = nums[0]
        curr_count = 1
        for num in nums[1:]:
            curr_count = curr_count + 1 if curr_num == num else curr_count - 1
            if curr_count == 0:
                curr_num = num
                curr_count += 1
        return curr_num