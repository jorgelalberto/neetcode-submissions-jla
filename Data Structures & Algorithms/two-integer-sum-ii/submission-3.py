class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            numSum = numbers[l] + numbers[r]
            if numSum == target:
                return [l + 1, r + 1]
            l = l + 1 if numSum < target else l
            r = r - 1 if numSum > target else r