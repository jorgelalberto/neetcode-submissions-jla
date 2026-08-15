class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        We know nums[0] is always rotated bc "rotated btwn 1 and n times"
        - above I don't think relevant -
        We can calculate rotations as below bc nums sorted
        rotations = min(nums)_ind * except for n rotations *
        then use ind to get num
        """
        # find min num
        l = 0
        r = len(nums)-1
        min_num_ind = 0
        while l<=r:
            mid = (l+r)//2
            min_num_ind = mid if nums[mid]<nums[min_num_ind] else min_num_ind
            # non-sorted
            if nums[l]>nums[r]:
                if nums[l]<=nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            # sorted
            else:
                return min(nums[l],nums[min_num_ind])

        return nums[min_num_ind]
