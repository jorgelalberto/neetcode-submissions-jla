class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        left = right = 1

        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]
            
            ans[-(i+1)] *= right
            right *= nums[-(i+1)]
        return ans