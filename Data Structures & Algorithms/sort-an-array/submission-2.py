class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums: List[int], l: int, r: int):
            i, j, k = 0, 0, l
            m = (l + r)//2
            left = nums[l:m+1]
            right = nums[m+1:r+1]

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            return nums

        def mergeSort(nums: List[int], l: int, r: int) -> None:
            if l == r:
                return

            m = (l + r)//2
            mergeSort(nums, l, m)
            mergeSort(nums, m+1, r)
            merge(nums, l, r)

        mergeSort(nums, 0, len(nums)-1)
        return nums