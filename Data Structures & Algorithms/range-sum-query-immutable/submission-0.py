class NumArray:

    def __init__(self, nums: List[int]):
        self.sumLeft = [0] * len(nums)
        self.sumRight = [0] * len(nums)
        self.sumTotal = sum(nums)

        for i in range(1, len(nums)):
            self.sumLeft[i] = self.sumLeft[i-1] + nums[i-1]

        for i in reversed(range(0, len(nums)-1)):
            self.sumRight[i] = self.sumRight[i+1] + nums[i+1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sumTotal - (self.sumLeft[left] + self.sumRight[right])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)