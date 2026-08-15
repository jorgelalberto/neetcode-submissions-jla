class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            print(l,r)
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # sorted
            elif nums[l]<nums[r]:
                l = mid+1 if nums[mid]<target else l
                r = mid-1 if nums[mid]>target else r
            # non-sorted
            else:
                # in left sorted
                if nums[l]<=nums[mid]:
                    # search left
                    if nums[l] <= target < nums[mid]:
                        r = mid-1
                    # search right
                    else:
                        l = mid+1
                # in right sorted
                else:
                    # search right
                    if nums[mid] < target <= nums[r]:
                        l = mid+1
                    # search left
                    else:
                        r = mid-1
        return -1