class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        left = [nums[0]]*len(nums)
        right = [nums[-1]]*len(nums)

        for i in range(1,len(nums)):
            left[i] = nums[i]*left[i-1]
            ans[i] *= left[i-1]
            right[-(i+1)] = nums[-(i+1)]*right[-i]
            ans[-(i+1)] *= right[-i]
        ans[0] = right[1]
        ans[-1] = left[-2]
        return ans