class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 if len(nums1)<=len(nums2) else nums2
        B = nums1 if len(nums1)>len(nums2) else nums2

        l = 0
        r = len(A)-1
        tot = len(nums1) + len(nums2)
        half = tot//2
        while True:
            mid = (l+r)//2
            midB = half - mid - 2

            Amid = A[mid] if mid>=0 else float("-infinity")
            Anext = A[mid+1] if mid+1<len(A) else float("infinity")
            Bmid = B[midB] if midB>=0 else float("-infinity")
            Bnext = B[midB+1] if midB+1<len(B) else float("infinity")

            if Amid <= Bnext and Bmid <= Anext:
                return min(Anext, Bnext) if tot%2==1 else (max(Amid,Bmid)+min(Anext,Bnext))/2
            elif Amid > Bnext:
                r = mid-1
            else:
                l = mid+1