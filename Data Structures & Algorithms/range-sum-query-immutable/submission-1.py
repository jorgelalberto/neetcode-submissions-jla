class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [0] * len(nums)
        for i in range(1, len(nums)):
            self.prefixSum[i] = self.prefixSum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] + self.prefixSum[right] - self.prefixSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)