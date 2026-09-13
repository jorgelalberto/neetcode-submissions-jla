class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        def twoSum(start: int, target: int) -> List[tuple]:
            l = start
            r = len(nums) - 1
            res = []

            while l < r:
                numSum = nums[l] + nums[r]
                if numSum == target:
                    res.append((nums[l], nums[r]))
                    l += 1
                    r -= 1
                l = l + 1 if numSum < target else l
                r = r - 1 if numSum > target else r
            return res

        quads = set()
        for i in range(len(nums)-3):
            for j in range(i + 1, len(nums)-2):
                temp = target - nums[i] - nums[j]
                twos = twoSum(j + 1, temp)
                if len(twos) != 0:
                    for twos1, twos2 in twos:
                        quads.add((nums[i], nums[j], twos1, twos2))
        return list(quads)