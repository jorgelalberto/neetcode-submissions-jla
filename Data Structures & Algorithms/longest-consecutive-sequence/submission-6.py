class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_cnt = 0
        cnt = 0
        for num in nums:
            if num-1 in nums:
                continue

            cnt = 0
            while num in nums:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                num += 1

        return max_cnt