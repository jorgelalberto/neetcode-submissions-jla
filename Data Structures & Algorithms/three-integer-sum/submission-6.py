class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []

        for i, num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                threeSum = nums[l] + nums[r] + num
                if threeSum < 0:
                    l += 1
                    continue
                elif threeSum > 0:
                    r-=1
                    continue
                triplets.append([nums[l], nums[r], num])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1

        return triplets