class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        totVals = 0
        i = 0
        while i<len(nums)-totVals:
            if nums[i] == val:
                totVals += 1
                nums[i] = nums[-totVals]
            else:
                i += 1
        return len(nums)-totVals