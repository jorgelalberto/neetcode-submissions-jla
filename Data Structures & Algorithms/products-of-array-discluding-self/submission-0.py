class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [nums[0]]*len(nums)
        right_arr = [nums[-1]]*len(nums)

        for i in range(1,len(nums)):
            left_arr[i] = nums[i]*left_arr[i-1]

        for i in reversed(range(0,len(nums)-1)):
            right_arr[i] = nums[i]*right_arr[i+1]

        nums[0] = right_arr[1]
        nums[-1] = left_arr[-2]
        for i in range(1,len(nums)-1):
            nums[i] = left_arr[i-1]*right_arr[i+1]
        return nums