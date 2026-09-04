class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            i, j, k = 0, 0, 0
            mergedNums = [0] * (len(right)+len(left))
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    mergedNums[k] = left[i]
                    i += 1
                else:
                    mergedNums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                mergedNums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                mergedNums[k] = right[j]
                j += 1
                k += 1
            return mergedNums

        def mergeSort(l, r):
            if l == r:
                return [nums[l]]

            m = (l + r)//2
            right = mergeSort(l, m)
            left = mergeSort(m+1, r)
            return merge(right, left)

        return mergeSort(0, len(nums)-1)